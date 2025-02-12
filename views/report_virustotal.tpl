% rebase("base.tpl", title=title)

<div>
  <h1> 
    {{ title }}
  </h1>
</div>



<div>
  <h3> 
    Список антивирусов, которые обнаружили угрозы.
  </h3> 
  <div>
  {{ ", ".join(detected.keys()) }}
  </div>
</div>

<div>
  <h3> 
    Сравните результаты с заданным списком антивирусов ?? 
  </h3>
  <h4> 
    Обнаруженные уязвимости
  </h4>
    <div>
      <table class="font-small">
        % for dk in detected.keys():
        <tr>
          <td>
            <span>
            {{ dk }}
            </span>
          </td>
          <td>
            <span class="color-blue">
            {{ detected[dk] }}
            </span>
          </td>
        </tr>
        % end
      </table>
    </div>
</div>

<div>
  <h3> 
    Ключевые моменты из отчёта VirusTotal Sandbox о поведении вредоноса.
  </h3>

      <div>
        <h4> 
          Cписок доменов и IP-адресов, с которыми вредонос общается.
        </h4>


      <table class="font-small" >
        <tr>
          <th>
          Hostname
          </th>
         <th>
          IP
          </th>
        </tr>
        % for t in dns_lookups:
        <tr>
          <td>
            <span>
            {{ t["hostname"] }}
            </span>
          </td>
          <td>
            <span class="color-blue">
            {{ ", ".join(t["resolved_ips"]) }}
            </span>
          </td>
        </tr>
        % end
      </table>

    </div>

      <div>
        <h3> 
          Использованные техники атак:
        </h3>
      <table class="font-small">
        % for at in attack_techniques:
        <tr>
          <td>
            <span>
              <a href="https://attack.mitre.org/techniques/{{at}}/" title="{{at}}" target="_blank">
                {{ at }}
              </a>
            </span>
          </td>

        </tr>
        % end
      </table>
    </div>

</div>


<div>
  <h3> 
    Файл проанализирован следущими сендбоксами:
  </h3>
  <table class="font-small">
    <tr>
      <td>
        <span>
          <span class="color-blue">
          {{ ", ".join(sandbox_names) }}
          </span>
        </span>
      </td>
    </tr>
  </table>
</div>


