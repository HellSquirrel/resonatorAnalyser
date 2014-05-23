require.config({
    baseUrl:'/static/scripts/',

    paths: {
        'jquery': '/static/scripts/libs/jquery',
        'bootstrap': '/static/scripts/libs/bootstrap.min',
        'underscore': '/static/scripts/libs/underscore-min',
        'backbone': '/static/scripts/libs/backbone-min',
        'jqui': '/static/scripts/libs/jquery-ui-1.10.4.custom.min'

    },

    shim: {
        "bootstrap": {
            deps: ["jquery"],
            exports: "$.fn.popover"
        },

        underscore: {
            exports: '_'
        },

        backbone: {
            deps: ["underscore", "jquery"],
            exports: "Backbone"
        },

        jqui: {
            deps: ['jquery']
        }
    }
});

require(['libs/binder','bootstrap'],
    function(binder, bootstrap){
        binder.bindAll(document, function(){});
});