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
    type: "string"
  ]
  proxy:
    type: "direct"
    api:
        create: "NXDB.db_create"
        read:   "NXDB.db_fetch"
        update: "NXDB.db_create"
        delete: "NXDB.db_delete"

    paramOrder: "id"

