define(function (require, exports) {
    var observer = require('libs/observer'),
        generator = require('libs/templateOperator');

    function createWidget(eventName) {

        return function(container, template){

            function render(parameters) {
                generator.generate(template, parameters, container)
            }

            observer.subscribe(eventName, render);
        };

    }

    exports.createWidget = createWidget;

});