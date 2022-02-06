# Generated table

<table>
<!-- <colgroup>
<col width="30%" />
<col width="70%" />
</colgroup> -->
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
<th>Link</th>
<th>License</th>
<th>Activity</th>
<th>Version</th>
<th>Project focus</th>
<th>Test framework</th>
</tr>
</thead>
<tbody>
{% for project_hash in site.data.projects -%}
{% assign project = project_hash[1] -%}
<!-- Tease out URL components for composing badge URLs -->
{% assign urlarray = project.repo_url | split : "/" %}
{% assign forgeurlarray = urlarray[2] | remove: "www." | split : "." %}
{% assign forge = forgeurlarray[0] %}
{% assign user = urlarray[3] %}
{% assign repo = urlarray[4] %}
<tr>

<td>{{ project.name }}</td>
<td>{{ project.description }}</td>
<td markdown="span">
[repo]({{ project.repo_url }}){% if project.docs_url %} /[docs]({{ project.docs_url }}) {% endif %}
</td>
<td markdown="span"> {{ project.license }} </td>
<!-- Activity: show last commit, commits/year -->
<td markdown="span">{% if forge == "github" %}
![Last commit](https://img.shields.io/{{forge}}/last-commit/{{user}}/{{repo}})
![commits/yr](https://img.shields.io/{{forge}}/commit-activity/y/{{user}}/{{repo}})
{% endif %}
</td>
<!-- Version/release information -->
<td markdown="span">{% if forge == "github" %}
![Last release date](https://img.shields.io/{{forge}}/release-date/{{user}}/{{repo}})
![Last release](https://img.shields.io/{{forge}}/v/release/{{user}}/{{repo}})
{% endif %}
</td>
<td>{{ project.project_focus }}</td>
<td>{{ project.test_framework }}</td>
</tr>
{% endfor %}
</tbody>
</table>

# Overview table

{% include_relative converted_table.md %}

Note: The original version of the table lived at https://ethercalc.net/1anmq248ktu6
