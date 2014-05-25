define(function (require, exports) {

    var observer = require('libs/observer');

    function notify() {
        observer.publish('events.parameters.changed');
    }

    function validate() {
        return !($(':invalid')).length;
    }


    exports.create = function(container) {
        container.on('input', function() {
            if(validate()) {
                notify();
            }
        })
    }
});