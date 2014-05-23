define(function (require, exports) {
    var observer = require('libs/observer'),
        renderer = require('libs/templateOperator'),
        settings = require('settings');

    function showError(container, template, message, details) {
        renderer.generate(template, { error: message, details: details }, container);
    }

    function listen(event, errorMsg, container, template) {

        observer.subscribe(event, function(errorDetails){
            showError(container, template, errorMsg, errorDetails)
        });

    }

    function create(container, template) {

        for (var i= 0; i< settings.errors.length; i++) {
            listen(settings.errors[i].event, settings.errors[i].message, container, template);
        }

    }

    exports.create = create
});

