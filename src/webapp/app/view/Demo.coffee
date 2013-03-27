Ext.define 'NXDirect.view.Demo',
    extend: 'Ext.grid.Panel'
    alias:  'widget.demo'

    initComponent: ->
        console.log "DemoView::initComponent: view initialized"
        @callParent(arguments)

    columns: [
        dataIndex: 'id'
        text:      'ID'
        width:     50
    ,
        dataIndex: 'name'
        text:      'Name'
        flex:      1
    ]

    store:
        model: "NXDirect.model.Demo"

# vim: set ft=coffee ts=4 sw=4 expandtab :

