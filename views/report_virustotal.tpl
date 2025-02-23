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
    Список антивирусов, которые не обнаружили угрозы.
  </h3> 
  <div>
    {{ ", ".join(not_detected.keys()) }}
  </div>
</div>



<div>
  <h3> 
    Сравнение с заданным списком.
  </h3> 
% for k in comparison_list.keys():
 
 <table style="width:100%">
  <tr>
    <td style="width:10%">
      <span>
        {{ k }}
      </span>
    </td>
    <td>
      <span class="{{ "color-red" if comparison_list[k] else "color-green" }}">
        {{ "обнаружил" if comparison_list[k] else "не обнаружил" }}
      </span>
    </td>
  </tr>
<table>
 
 
% end
</div>



<div>
  <h4> 
    Обнаруженные уязвимости
  </h4>

  <table style="width:100%">
    % for dk in detected.keys():
    <tr>
      <td style="width:15%">
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


<div>
  <h3> 
    Ключевые моменты из отчёта VirusTotal Sandbox о поведении вредоноса.
  </h3>

  <h4> 
    Cписок доменов и IP-адресов, с которыми вредонос общается.
  </h4>

  <table style="width:100%">
    <tr class="bold flex">
      <td style="width:20%">
        Hostname
      </td>
      <td>
        IP
      </td>
    </tr>
    % for t in dns_lookups:
    <tr class="flex">
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

  <h3> 
    Использованные техники атак:
  </h3>


  <div class="font-small">
    % for at in attack_techniques:
    <div class="flex">

      <div>
        <a href="https://attack.mitre.org/techniques/{{at}}/" title="{{at}}" target="_blank">
          {{ at }}
        </a>
      </div>

    </div>
    % end
  </div>

</div>


<div>
  <h3> 
    Файл проанализирован следущими песочницами:
  </h3>
  <div>
    <div>
      <div>
        <span>
          <span class="color-blue">
          {{ ", ".join(sandbox_names) }}
          </span>
        </span>
      </div>
    </div>
  </div>
</div>


