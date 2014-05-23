define(function (require, exports) {

    var factory = require('widgets/factories/resultWidget'),
        settings = require('settings');

    exports.create = factory.createWidget('events.misalignments.tab.activated', 'misalignments', settings.urls.MISALIGNMENTS_URL,
        settings.selectors.MISALIGNMENTS_PARAMS);
});