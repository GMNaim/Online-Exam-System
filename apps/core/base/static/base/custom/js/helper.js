class Helper {

    constructor() {
        this._storage = new Storage();
        // this._user = this.storage.getStorage('local', '_arU');
    }

    get storage() {
        return this._storage;
    };

    toast = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.addEventListener('mouseenter', Swal.stopTimer)
            toast.addEventListener('mouseleave', Swal.resumeTimer)
        }
    });

    httpRequestWithoutHeaders(url, method, inputs, contentType) {
        method = method || 'GET';
        inputs = inputs || '';
        contentType = contentType || "application/json";
        let obj = {
            url: url,
            type: method,
            data: inputs,
            cache: true,
            dataType: 'json',
            crossDomain: true,
            ifModified: true,
        };

        if (contentType !== 'false') {
            obj.contentType = contentType;
        }

        return $.ajax(obj);
    };

    httpRequest(url, method, inputs, contentType) {
        $.ajaxSetup({
            headers: {'Authorization': 'JWT ' + this.storage.getStorage('local', 'token').access},
            error: function (x, status, error) {
                if (x.status === 401) {
                    if (error === "Unauthorized") {
                        $(document).ajaxComplete($.unblockUI);
                        alert("Sorry, your session has expired. Please login again to continue");
                        window.location.href = "/logout/";
                    }
                }
            }
        });

        method = method || 'GET';
        inputs = inputs || '';
        contentType = contentType || "application/json";
        let obj = {
            url: url,
            type: method,
            data: inputs,
            cache: true,
            dataType: 'json',
            crossDomain: true,
            ifModified: true,
        };

        if (contentType !== 'false') {
            obj.contentType = contentType;
        }
        return $.ajax(obj);
    };


    blockUI() {
        $.blockUI({
            message: '<div class="spinner-grow text-primary" role="status"><span class="sr-only">Loading...</span></div><div class="spinner-grow text-warning" role="status"><span class="sr-only">Loading...</span></div></div><div class="spinner-grow text-success" role="status"><span class="sr-only">Loading...</span></div><div class="spinner-grow text-danger" role="status"><span class="sr-only">Loading...</span></div>',
            // styles for the overlay
            overlayCSS: {
                zIndex: 2147483646,
                backgroundColor: 'white',
                opacity: 0.8,
                cursor: 'wait'
            },
            css: {
                zIndex: 2147483647,
                top: ($(window).height() - 400) / 1.2 + 'px',
                left: ($(window).width() - 400) / 1.8 + 'px',
                width: '400px',
                backgroundColor: 'rgba(0, 0, 0, 0)',
                border: '0px',
            }
        });
    };
}