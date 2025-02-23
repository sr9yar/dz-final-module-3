% rebase("base.tpl", title=title)

<div>
  <h1> 
    {{ get("title", "Title") }}
  </h1>
</div>


<div>
% for p in data["programs"]:
  <div class="bold color-blue">
    Название программы: {{ p["name"] }}
  </div>
  <div>
    Версия программы: {{ p["version"] }}
  </div>

  % if len(p["cve"]) == 0:
    <div class="mb-1">
      {{ "Уязвимостей не обнаружено. " }}
    </div>
  % end

  % if len(p["cve"]) > 0:
    <div>
      Список CVE (Всего {{len(p["cve"])}}):
    </div>
    <div>
      <span class="subtitle">
        Общедоступная информация по эксплойтам содержится по ссылкам.
      </span>
    <div>
  % end

  % if len(p["cve"]) > 0:
    <div class="mb-1">
      <ul class="font-small">
        % for v in p["cve"]:
          <li class="mb-01">
            <a href="https://vulners.com/cve/{{v["id"]}}" title="{{v["title"]}}" target="_blank">
              {{ v["title"] }}
            </a>
          </li>
        % end
      </ul>
    </div>
  % end

% end
</div>


