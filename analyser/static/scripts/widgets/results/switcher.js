define(function (require, exports) {
    var observer = require('libs/observer');

    function create(container) {

        var event = container.attr('data-event');
        container.on('show.bs.tab', function() {
            observer.publish(event);
        });

    }

    exports.create = create;
});