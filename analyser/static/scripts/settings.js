define(function (require, exports) {

    exports.errors = [
        { event: 'events.error.server.fail', message: 'На сервере произошла ошибка!' }
    ];

    exports.urls = {
        MATRIX_URL: '/matrix',
        MISALIGNMENTS_URL: '/misalignments'
    };

    exports.selectors = {
        MIRROR_PARAMS: '.mirror-parameter',
        MISALIGNMENTS_PARAMS: '.mis-parameter'
    }

});