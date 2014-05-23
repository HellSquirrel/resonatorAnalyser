define(function (require, exports) {
    var observer = require('libs/observer');

    var DELAY = 500;

    function publisher(parameters, eventName) {

        return setTimeout(function() {
            observer.publish(eventName, parameters);
        }, DELAY);

    }



    function createWidget(eventName) {

        return function (container) {
            var timer;

            function onchange() {
                var value = container.val();

                timer && (timer = clearTimeout(timer));

                if (container.is(':invalid')) {
                    return;
                }

                var parameters = {};
                parameters[container.attr("name")] = value;

                timer = publisher(parameters, eventName);
            }

            container.on('input', onchange);

            //если у поля есть значение по умолчанию, сразу нарисовать
            if(container.val()) onchange();
        }
    }

        exports.createWidget = createWidget;
});