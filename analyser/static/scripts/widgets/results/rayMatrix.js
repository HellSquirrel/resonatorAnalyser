define(function (require, exports) {

    var factory = require('widgets/factories/resultWidget'),
        settings = require('settings');

    exports.create = factory.createWidget('events.matrix.tab.activated', 'matrix', settings.urls.MATRIX_URL,
        settings.selectors.MIRROR_PARAMS);
});