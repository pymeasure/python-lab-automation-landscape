# Generated table


Name | Description | Repo URL
--- | --- | ---
{% for project_hash in site.data.projects -%}
{% assign project = project_hash[1] -%}
{{ project.name }} | {{ project.description }}  | [repo]({{ project.repo_url }})
{% endfor %}

# Overview table

{% include_relative converted_table.md %}

Note: The original version of the table lived at https://ethercalc.net/1anmq248ktu6
