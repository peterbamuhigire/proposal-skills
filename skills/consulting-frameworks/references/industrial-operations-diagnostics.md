# Industrial Operations Diagnostics

Use this reference when a proposal concerns manufacturing, food processing, warehousing, inventory management, ERP/MES/WMS/TMS, production planning, distribution, facilities layout, material handling, or operational sustainability.

## Diagnostic Domains

| Domain | What to assess | Typical evidence |
|---|---|---|
| Demand and service | Demand pattern, service promises, forecast quality, stockout or late-delivery history | Sales history, order book, forecast files, customer service reports |
| Materials and inventory | BOMs, recipes, safety stock, reorder points, lead times, MOQ, expiry, slow stock | Item master, stock ledger, purchase orders, warehouse counts |
| Production planning | MPS/MRP logic, production orders, batch sizes, time fences, pegging | Production plan, BOMs, routings, planned orders |
| Scheduling and capacity | Work-centre calendars, setup/changeover, rated output, bottlenecks, maintenance blocks | Job cards, machine logs, maintenance records |
| Warehouse execution | Receiving, putaway, storage, picking, staging, dispatch, returns | Layout, bin list, pick slips, stock movement records |
| Logistics network design | Supplier/customer geography, facilities, lanes, nodes, service-level promises, cross-dock or regional stocking logic | Network map, shipment history, delivery zones, service-level commitments, cost-to-serve data |
| Transportation management | Mode selection, carrier strategy, route planning, fleet utilisation, consolidation, dispatch, tracking, freight claims | Carrier contracts, route plans, fleet logs, freight bills, PODs, GPS/telematics data, claims records |
| Trade, customs, and documentation | Incoterms, customs broker use, import/export documents, duties, risk transfer, bonded or regulated goods controls | Commercial invoices, packing lists, BOL/waybills, customs declarations, broker files, clearance records |
| Logistics service providers | 3PL/4PL/lead logistics provider scope, SLAs, escalation model, data integration, performance governance | LSP contracts, SLA reports, integration specs, carrier scorecards, issue logs |
| Facilities and flow | Layout, aisle constraints, movement distance, congestion, safety, future expansion | Site walk-through, spaghetti diagram, from-to chart |
| Quality and traceability | Incoming inspection, in-process control, batch release, NCRs, recall readiness | QC records, CoAs, batch records, complaint logs |
| Green operations | Energy, water, yield, scrap, rework, waste, by-product recovery | Utility bills, production reports, waste manifests |

## Methodology Building Blocks

### Current-State Assessment

- Map the order-to-delivery and procure-to-produce processes.
- Build a material-flow map from receiving to dispatch.
- Reconcile system stock, physical stock, WIP, and financial inventory value.
- Identify bottlenecks using throughput, queue time, utilisation, and quality loss.
- Review master data quality for items, suppliers, BOMs, recipes, routings, UOM, and locations.

### Planning and Scheduling Review

- Check whether sales forecasts translate into a master production schedule.
- Test whether gross material requirements are netted against available stock and scheduled receipts.
- Review safety-stock, reorder-point, MOQ, and lot-sizing assumptions.
- Assess whether production schedules reflect setup, changeover, maintenance, and labour constraints.
- Identify exception-management gaps: shortages, excess, expedite, defer, cancel, reschedule, and overload.

### Warehouse and Facilities Review

- Assess receiving, quarantine, storage, picking, packing, dispatch, returns, and cycle-count workflows.
- Review storage policy, bin capacity, FEFO/FIFO rotation, cold-chain or hazardous-material separation.
- Use a from-to or material-flow view to identify unnecessary movement, double handling, and congestion.
- Identify quick wins before automation: layout change, slotting, replenishment triggers, pick-path logic.

### Logistics Network and Transportation Review

- Map the end-to-end logistics network: suppliers, ports, borders, factories, warehouses, branches, cross-docks, customers, lanes, modes, and carriers.
- Test whether the promised service level is supported by inventory position, replenishment frequency, transport capacity, route design, and warehouse throughput.
- Compare own-fleet, for-hire carrier, courier, freight forwarder, 3PL, 4PL, and lead-logistics-provider options against cost, control, reliability, compliance, and scalability.
- Review shipment lifecycle controls: booking, BOL or waybill, labels, pickup, track-and-trace, expediting, consolidation, proof of delivery, claims, returns, and reverse logistics.
- Assess transport and carrier KPIs: on-time pickup, on-time delivery, OTIF, cost per order/unit/km, load utilisation, route adherence, damage rate, claims rate, and exception closure time.
- For import/export scopes, review Incoterms, customs broker role, clearance lead times, duty assumptions, document completeness, and transfer of cost/risk.

### Green and Cost-to-Serve Review

- Calculate energy per unit, water per unit, yield, scrap, rework, and waste cost where data exists.
- Link resource losses to gross margin, working capital, compliance exposure, and customer service.
- Identify circular-economy options such as by-product sale, reuse, recycling, composting, or energy recovery.

## Proposal Language

"Our methodology will assess the client's industrial and logistics operating model across demand, materials, capacity, warehouse execution, logistics network design, transportation, documentation controls, quality, and resource efficiency. This allows us to identify whether performance constraints are caused by demand volatility, material shortages, planning rules, factory capacity, warehouse flow, carrier performance, route design, inventory positioning, trade-documentation gaps, quality losses, or sustainability cost leakage before recommending systems or capital expenditure."

## Deliverable Options

- Industrial operations diagnostic report
- MRP and inventory-policy assessment
- Production scheduling and capacity model
- Warehouse and material-flow improvement plan
- Logistics network and cost-to-serve assessment
- Transportation, carrier, and fleet strategy
- Import/export documentation and customs-control review
- 3PL, 4PL, or lead-logistics-provider operating model
- Factory layout and handling concept note
- Quality and traceability controls matrix
- Green production and resource-efficiency roadmap
- ERP/MES/WMS/TMS requirements brief
