#!/usr/bin/env python3
"""Validate scoped claim records and fail on overdue review; no semantic approval."""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Longest gap allowed between verification and the next review, by freshness class.
MAX_REVIEW_GAP_DAYS = {'volatile': 45, 'stable': 365}


def validate_records(records, today):
    errors = []
    seen = set()
    if not isinstance(records, list) or not records:
        return ['source register must contain records']
    for row in records:
        try:
            identifier = row['id']
            if identifier in seen:
                raise ValueError('duplicate source id')
            seen.add(identifier)
            for field in ('url', 'claim', 'source_version', 'freshness_class', 'review_date', 'support_state', 'uncertainty', 'owner'):
                if not isinstance(row[field], str) or not row[field].strip():
                    raise ValueError(f'missing {field}')
            review = date.fromisoformat(row['review_date'])
            if today > review:
                errors.append(f'{identifier}: review expired')
            if not row['url'].startswith('https://'):
                raise ValueError(f'{identifier}: url must be https')
            if row['freshness_class'] not in MAX_REVIEW_GAP_DAYS:
                raise ValueError(f'{identifier}: unknown freshness class')
            if row['support_state'] not in ('SCOPED', 'NOT_ASSESSED'):
                raise ValueError('invalid support state')
            if row['support_state'] == 'NOT_ASSESSED' and row.get('verified_date'):
                raise ValueError(f'{identifier}: NOT_ASSESSED must not carry a verified date')
            if row['support_state'] == 'SCOPED':
                accessed = date.fromisoformat(row['access_date'])
                verified = date.fromisoformat(row['verified_date'])
                if not accessed <= verified <= today or review < verified:
                    raise ValueError('inconsistent verification dates')
                if (review - verified).days > MAX_REVIEW_GAP_DAYS[row['freshness_class']]:
                    raise ValueError(f'{identifier}: review date is too far after verification')
        except (KeyError, ValueError, TypeError) as exc:
            errors.append(f'invalid source record: {exc}')
    return errors


def validate(root=ROOT):
    try:
        data = json.loads((root / 'docs/source-registers/2026-10-currentness.json').read_text())
        return validate_records(data['records'], date.today())
    except (OSError, ValueError, KeyError) as exc:
        return [f'source register unavailable: {exc}']


if __name__ == '__main__':
    errors = validate()
    print('\n'.join(errors) if errors else 'source currency metadata: PASS; semantics remain scoped')
    raise SystemExit(bool(errors))
