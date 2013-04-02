Ext.define "NXDirect.store.Direct",
  extend: "Ext.data.Store"
  model:  "NXDirect.model.Demo"
  autoLoad: yes
  proxy:
    type: "direct"
    api:
        create: "NXDB.db_create"
        read:   "NXDB.db_fetch"
        update: "NXDB.db_update"
        delete: "NXDB.db_delete"
    reader:
        type: "json"
        root: "items"

    paramOrder: "id"
