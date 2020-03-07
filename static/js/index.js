function NewProjects() {

}


NewProjects.prototype.run = function () {
    var self = this;
    self.listenAddProjectsEvent();
};

NewProjects.prototype.listenAddProjectsEvent = function () {
    var addBtn = $("#add-project-btn");
    addBtn.click(function () {

        var projectName = $("#project_name").val();
        var projectDesc = $("#project_desc").val();

        xfzajax.post({
            'url': '/mock/project/',
            'name': projectName,
            'desc': projectDesc,
            'data': {
                'name': projectName,
                'desc': projectDesc,
            },
            'success': function (result) {
                if (result['message'] === "SUCCESS" ) {
                    window.location.reload();
                    window.messageBox.showSuccess("评论发表成功！");
                } else {
                    window.messageBox.showError(result['message']);
                }
            }
        });
    });
};


$(function () {
    var project = new NewProjects();
    project.run();
});