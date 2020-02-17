function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length ; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')){
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var myajax = {
    'get': function (args) {
        args['method'] = 'get';
        this.ajax(args);
    },

    'post': function (args) {
        args['method'] = 'post';
        this._ajaxSetup();
        this.ajax(args);
    },

    'ajax': function (args) {
        $.ajax(args);
    },

    '_ajaxSetup': function () {
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/.test(settings.type) && !this.crossDomain){
                    xhr.setRequestHeader('X-CSRFToken', getCookie('csrftoken'));
                }
            }
        })
    }
};