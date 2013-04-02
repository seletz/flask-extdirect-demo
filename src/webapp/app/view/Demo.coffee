Ext.define 'NXDirect.view.Demo',
    extend: 'Ext.grid.Panel'
    alias:  'widget.demo'

    columns: [
        dataIndex: 'id'
        text:      'ID'
        width:     50
    ,
        dataIndex: 'name'
        text:      'Name'
        flex:      1
        editor:
            allowBlank: no
            xtype: "textfield"
    ,
        dataIndex: 'number'
        text:      'Number'
        flex:      1
        editor:
            allowBlank: no
            xtype: "numberfield"
    ]

    store: "Direct"

    initComponent: ->
        console.log "DemoView::initComponent: view initialized"
        window.view = @

        rowEditing = Ext.create 'Ext.grid.plugin.RowEditing',
            clicksToMoveEditor: 1
            autoCancel: false

        @plugins = [rowEditing]

        @callParent(arguments)


# vim: set ft=coffee ts=4 sw=4 expandtab :

