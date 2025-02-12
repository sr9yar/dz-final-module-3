% rebase("base.tpl", title="Главная")

<div>
  <h1> 
    {{ title }}
  </h1>
</div>

<div>
  <ul>
    % for item in links:
      <li>
        <a href="{{ item["url"] }}" title="{{ item["anchor"]}}" target="{{ item["target"] }}">
          {{ item["anchor"] }}
        </a>
      </li>
    % end
  </ul>
</div>

