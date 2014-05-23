//this module binds javascript object with dom container and template
//object declaration : module.object

define(['jquery', 'underscore'], function ($, _) {
    var BOUND_CONTAINER_CLASS = 'data-bound-container';
    var BOUND_OBJECTS_ATTRIBUTE = 'data-bound-objects';
    var TEMPLATE_ATTRIBUTE = 'data-template';



    function bind(object, container, template, onLoad){
        var names = object.split('.');
        var moduleName = names[0];
        var functionName = names[1];

        require([moduleName],function(module){
            if (functionName){
                (module[functionName])(container, template);
            } else {
                module.create($(container), template);
            }

            onLoad();
        });
    }

    function calculateObjects(element){
        var total = 0;
        _.each(element.querySelectorAll('.' + BOUND_CONTAINER_CLASS), function(container){
            total += container.getAttribute(BOUND_OBJECTS_ATTRIBUTE).split(/[ +\t+\n+\r+]+/).length;
        });

        return total
    };

//binds all bound objects in element then proceed callback
    function bindAll(element, callback){
        var objectsBound = 0;
        var total = calculateObjects(element);
        var boundContainers = element.querySelectorAll('.' + BOUND_CONTAINER_CLASS);

        //for every container
        _.each(boundContainers, function(container){
            var bound = container.getAttribute(BOUND_OBJECTS_ATTRIBUTE);

            var template = container.getAttribute(TEMPLATE_ATTRIBUTE);

            if(!bound) throw new Error('boundContainer should contain boundObject');
            var boundObjects = bound.split(' ');

            //for every bound object
            _.each(boundObjects, function(boundObject){
                bind(boundObject, container, template, function() {
                    objectsBound += 1;

                        //debug info
                        console.log(objectsBound + "." +boundObject + ' bound');

                    if(objectsBound === total) {
                        callback && callback();

                    }
                });

            });

        })
    }


    return {
        bindAll: bindAll
    }
});