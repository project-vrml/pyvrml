from pyvrml.gitlab.gitlab import gitlab_auth
from pyvrml.http.httputils import get

git_token = "token"

# 监控gitlab项目pipeline执行情况
if __name__ == '__main__':
    # 登录gitlab
    gl = gitlab_auth()

    projects_name = ['test']
    for project_name in projects_name:

        projects = gl.projects.list(search=project_name)
        for project in projects:
            print("[project]: " + str(project))
            search_project_name = project.name
            if search_project_name != project_name:
                # 过滤非精确匹配的项目
                continue

            pipelines = project.pipelines.list(page=1, per_page=1)
            for pipeline in pipelines:
                # print("[pipeline1]: " + str(pipeline))

                pipeline = project.pipelines.get(pipeline.id)
                print("[pipeline]: " + str(pipeline))

                user_name = pipeline.user.get('name')
                web_url = pipeline.web_url
                status = pipeline.status
                # pipeline未通过
                if status != "success":
                    print(f"[{project_name}] pipeline健康检查失败!!!")

                # pipeline通过
                else:
                    commit_id = pipeline.sha
                    test_res = get(
                        url=f"http://git.com/group/{project_name}/commit/{commit_id}/pipeline_reports.json?type=test",
                        params=None,
                        headers={'PRIVATE-TOKEN': git_token})
                    print("[test]: " + str(test_res))

                    if test_res:
                        summary = test_res.get("summary")
                        if summary:
                            total = summary.get("total")
                            resolved = summary.get("resolved")
                            failed = summary.get("failed")
                            error = summary.get("error")
                            if failed > 0 or error > 0:
                                print(f"[{project_name}] test健康检查未通过!!!")
                            else:
                                print(f"[{project_name}] test健康检查通过~~~")
                        else:
                            print(f"[{project_name}] test健康检查获取失败!!!")
