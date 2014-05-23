define(function (require, exports) {
    var observer = require('libs/observer'),
        sender = require('actions/sender'),
        generator = require('libs/templateOperator');

    function loadContent(container, template, dataName, url, selector) {

        function draw (data) {

            var parameters = {};
            parameters[dataName] = data;

            generator.generate(template, parameters, container);
        }

        sender.getData(url, selector, draw)

    }


    function createWidget(eventName, dataName, url, selector) {
        return function(container, template) {

            observer.subscribe(eventName, function() {
                loadContent(container, template, dataName, url, selector);
            });

        }
    }

    exports.createWidget = createWidget;
});