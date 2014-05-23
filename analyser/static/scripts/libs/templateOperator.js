define(['jquery', 'underscore', 'libs/html'], function ($, _, html) {

    function prepareTemplate(templateId, parameters) {

        var template = _.template(document.getElementById(templateId).innerHTML);
        return template(parameters);
    }

    //заменяет содержимое контейнера шаблоном
    function generate(templateId, parameters, container) {

        var template = prepareTemplate(templateId, parameters);
        html.replace(template, container);
    }

    return {
        generate: generate
    }
});