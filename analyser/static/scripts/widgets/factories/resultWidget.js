define(function (require, exports) {
    var observer = require('libs/observer'),
        sender = require('actions/sender'),
        generator = require('libs/templateOperator');


    function draw (data, container, template, dataName) {

        var parameters = {};
        parameters[dataName] = data;

        generator.generate(template, parameters, container);
    }


    function createWidget(eventName, dataName) {

        return function(container, template) {

            observer.subscribe(eventName, function(data) {
                draw(data, container, template, dataName);
            });

        }
    }

    exports.createWidget = createWidget;
});