define(function(require, exports) {

    function collect(selector){
        var inputs = $(selector);
        var data = {};
        for (var i = 0; i < inputs.length; i++) {

            var input = inputs[i];
            var value = input.value;
            var name = input.getAttribute('name');

            if(name in data){

                data[name].push(value);
            }

            else{
                data[name] = [value];
            }
        }

        return data
    }

    exports.collect = collect
});