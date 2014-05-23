define(['jquery', 'config'], function ($, config) {

    var funcMapper = config.functionMap;

    function replaceFuncs(string) {
        return string.replace(/[a-z]+\(/gi,function(match) {
            return 'funcMapper.' + match;
        });
    }

    function replaceCells(string) {
        return string.replace(/[a-z]+[0-9]+/gi,function(match) {
            return document.querySelector('#' + match).value;
        });
    }

    function parse(string) {
        if(string.charAt(0) === '=') {

            var substring = string.substring(1);
            var compiled = replaceCells(substring);
            compiled = replaceFuncs(compiled);

            try{
                return eval(compiled);
            }

            catch(ex){
               return config.cellEvaluationError
            }
        }

        else return string;
    }

    return {
        parse: parse
    }
});