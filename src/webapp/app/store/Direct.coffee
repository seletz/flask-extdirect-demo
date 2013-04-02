Ext.define "NXDirect.store.Direct",
  extend: "Ext.data.Store"
  model:  "NXDirect.model.Demo"
  autoLoad: yes
  autoSync: yes
  proxy:
    type: "direct"
    api:
        create:  "NXDB.db_create"
        read:    "NXDB.db_fetch"
        update:  "NXDB.db_update"
        destroy: "NXDB.db_delete"
    reader:
        type: "json"
        root: "items"

    paramOrder: "id"

# vim: set ft=coffee ts=4 sw=4 expandtab :
