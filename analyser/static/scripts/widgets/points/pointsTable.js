define(function(require, exports) {
    var factory = require('widgets/factories/appearOnEventWidget');

    exports.create = factory.createWidget('event.points.number.changed', 'points');
});