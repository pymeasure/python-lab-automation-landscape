---
layout: page
title: "Catalog"
permalink: /catalog/
---
A structured overview over Python lab automation packages.

Presentation improvements are WIP.

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
<th>Communication types</th>
<th>Transport layers</th>
<th>Procedures?</th>
<th>GUI?</th>
<th>GUI library</th>
<th>Units?</th>
<th>Unit library</th>
<th>Instrument categories?</th>
<th>Remarks</th>
<th>Collected by</th>
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
<td>{{ project.communication_types }}</td>
<td>{{ project.transport_layers }}</td>
<td>{% if project.has_procedures == true %}
    &#10004;
    {% elsif project.has_procedures == false %}
    &#10007;
    {% else %}
    
    {% endif %}
</td>
<td>{% if project.has_gui == true %}
    &#10004;
    {% elsif project.has_gui == false %}
    &#10007;
    {% else %}
    
    {% endif %}
</td>
<td>{{ project.gui_technology }}</td>
<td>{% if project.has_unit_support == true %}
    &#10004;
    {% elsif project.has_unit_support == false %}
    &#10007;
    {% else %}
    
    {% endif %}
</td>
<td>{{ project.unit_library }}</td>
<td>{% if project.instrument_categories == true %}
    &#10004;
    {% elsif project.instrument_categories == false %}
    &#10007;
    {% else %}
    
    {% endif %}
</td>
<td>{{ project.remarks | markdownify }}</td>
<td>{{ project.collected_by }}</td>
</tr>
{% endfor %}
</tbody>
</table>

Note: The original version of the table lived at https://ethercalc.net/1anmq248ktu6
