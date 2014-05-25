define(function (require, exports) {
    var observer = require('libs/observer');
    var sender = require('actions/sender');

    function load(url, paramSelector, eventName) {

        sender.getData(url, paramSelector, function(data) {
            observer.publish(eventName, data);
        })
    }

    exports.create = function(container) {

        var url = container.attr('data-url');
        var parameterSelector = container.attr('data-collected');
        var onLoad = container.attr('data-on-load');

        container.click(function() {
            load(url, parameterSelector, onLoad);
        })
    }
});