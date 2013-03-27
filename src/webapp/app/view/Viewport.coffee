Ext.define "NXDirect.view.Viewport",
  renderTo: Ext.getBody()
  extend: "Ext.container.Viewport"
  requires: ["Ext.tab.Panel", "Ext.layout.container.Border"]
  layout:
    type: "border"

  items: [
    region: "west"
    xtype: "panel"
    title: "west"
    width: 150
  ,
    region: "center"
    xtype: "tabpanel"
    items: [
        xtype: "grid"
        title: "ExtDirect Demo"

        store:
            autoload: yes
            proxy:
                type: "direct"
                api:
                    create: "NXDB.db_create"
                    read:   "NXDB.db_fetch"
                    update: "NXDB.db_create"
                    delete: "NXDB.db_delete"

                paramOrder: "id"

        columns: [
            dataIndex: 'id'
            text:      'ID'
            width:     50
        ,
            dataIndex: 'name'
            text:      'Name'
            flex:      1
        ]
    ,
    ]
  ]

