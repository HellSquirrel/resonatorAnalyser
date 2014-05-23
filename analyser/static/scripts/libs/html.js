define(function (require, exports) {
    var binder = require('libs/binder');


    function replace(html, container) {
        container.html(html);
        binder.bindAll(container[0]);
    }

    exports.replace = replace;
});