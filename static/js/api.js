function NewApis() {

}


NewApis.prototype.run = function () {
    var self = this;
    self.listenAddApisEvent();
};

NewApis.prototype.listenAddApisEvent = function () {
    var addBtn = $("#add-api-btn");
    var editor = ace.edit("code");
    addBtn.click(function () {

        var apiName = $("#api_name").val();
        var apiRoute = $("#api_route").val();
        var apiType = $("#api_method").val();
        var apiProject = $("#api_project").val();
        var apiParams = editor.session.getValue();

        xfzajax.post({
            'url': '/mock/api/',
            'data': {
                'project_id': apiProject,
                'method': apiType,
                'name': apiName,
                'url': apiRoute,
                'body': apiParams
            },
            'success': function (result) {
                if (result['message'] === "SUCCESS") {
                    window.location.reload();
                    window.messageBox.showSuccess("创建接口成功!");
                } else {
                    window.messageBox.showError(result['message']);
                }
            }
        });
    });
};


$(function () {
    var api = new NewApis();
    api.run();
});