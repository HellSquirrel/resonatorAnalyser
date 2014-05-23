define([], function(){
   var bus = { };

   function subscribe(eventName, func ,tag) {

       if(bus[eventName]) {
           bus[eventName].push(func);
       }

       else {
           bus[eventName] = [func]
       }

       if(tag) {
           bus[eventName][bus[eventName].length-1].tag = tag;
       }

   }


   function unsubscribe(eventName, tag) {
       var callbacks = bus[eventName];

       if(callbacks){
           for (var i = 0; i < callbacks.length; i++) {
               var callback = callbacks[i];
               if(callback.tag === tag) {
                   callbacks.splice(i,1);
               }
           }
       }
   }

   function publish(eventName, data) {

       if(bus[eventName]){
           for (var i = 0; i < bus[eventName].length; i++) {
               (bus[eventName][i])(data);
           }
       }

   }

   return {
       publish: publish,
       subscribe: subscribe,
       unsubscribe: unsubscribe
   }
});
