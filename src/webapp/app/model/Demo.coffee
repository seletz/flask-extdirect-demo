Ext.define "NXDirect.model.Demo",
  extend: "Ext.data.Model"
  fields: [
    name: "id"
    type: "int"
  ,
    name: "name"
    type: "string"
  ,
    name: "number"
    type: "int"
  ]
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

# vim: set ft=coffee ts=4 sw=4 expandtab :

