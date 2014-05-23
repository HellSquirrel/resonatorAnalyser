define(function(require, exports) {

    var collector = require('actions/collector');
    var observer = require('libs/observer');

    function errorAlert() {
        observer.publish('events.error.server.fail', arguments[2]);
    }

    function jsonGet(url, params, callback) {
        var jsonParams = JSON.stringify(params);

        $.ajax({
            url: url + '?params=' + jsonParams,
            contentType: 'application/json',
            success: callback,
            error: errorAlert
        });

    }

    function getData(url, param_selector, callback) {

        var params = collector.collect(param_selector);
        jsonGet(url, params, callback);

    }

    exports.getData = getData;
});