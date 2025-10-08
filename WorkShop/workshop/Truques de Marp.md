---
marp: true
theme:
class:
paginate: true
size: 16:9
style: '/* @theme rose-pine-moon *//*Rosé Pine theme create by RAINBOWFLESH> www.rosepinetheme.comMIT License https://github.com/rainbowflesh/Rose-Pine-For-Marp/blob/master/licensepalette in :root*/@import "default";@import "schema";@import "structure";:root {    --base: #232136;    --surface: #2a273f;    --overlay: #393552;    --muted: #6e6a86;    --subtle: #908caa;    --text: #e0def4;    --love: #eb6f92;    --gold: #f6c177;    --rose: #ea9a97;    --pine: #3e8fb0;    --foam: #9ccfd8;    --iris: #c4a7e7;    --highlight-low: #2a283e;    --highlight-muted: #44415a;    --highlight-high: #56526e;    font-family: Pier Sans, ui-sans-serif, system-ui, -apple-system,        BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans,        sans-serif, "Apple Color Emoji", "Segoe UI Emoji", Segoe UI Symbol,        "Noto Color Emoji";    font-weight: initial;    background-color: var(--base);}/* Common style */h1 {    color: var(--rose);    padding-bottom: 2mm;    margin-bottom: 12mm;}h2 {    color: var(--rose);}h3 {    color: var(--rose);}h4 {    color: var(--rose);}h5 {    color: var(--rose);}h6 {    color: var(--rose);}a {    color: var(--iris);}p {    font-size: 20pt;    font-weight: 600;    color: var(--text);}code {    color: var(--text);    background-color: var(--highlight-muted);}text {    color: var(--text);}ul {    color: var(--subtle);}li {    color: var(--subtle);}img {    background-color: var(--highlight-low);}strong {    color: var(--text);    font-weight: inherit;    font-weight: 800;}mjx-container {    color: var(--text);}marp-pre {    background-color: var(--overlay);    border-color: var(--highlight-high);}/* Code blok */.hljs-comment {    color: var(--muted);}.hljs-attr {    color: var(--foam);}.hljs-punctuation {    color: var(--subtle);}.hljs-string {    color: var(--gold);}.hljs-title {    color: var(--foam);}.hljs-keyword {    color: var(--pine);}.hljs-variable {    color: var(--text);}.hljs-literal {    color: var(--rose);}.hljs-type {    color: var(--love);}.hljs-number {    color: var(--gold);}.hljs-built_in {    color: var(--love);}.hljs-params {    color: var(--iris);}.hljs-symbol {    color: var(--foam);}.hljs-meta {    color: var(--subtle);}'
---

---

## 1. Propriedades de Front-Matter YAML

Essas vão dentro do bloco `--- ... ---` no início do `.md`:

|Propriedade|Tipo / Valor|Descrição|
|---|---|---|
|`marp: true`|boolean|Ativa o modo de apresentação|
|`theme`|`default`, `gaia`, `uncover`, ou nome de tema custom|Define o tema base|
|`paginate`|`true` / `false`|Exibe numeração dos slides|
|`paginate-position`|ex: `bottom-right`|Define onde aparece a numeração|
|`size`|`16:9`, `4:3`, `A4`, `Letter`, etc.|Proporção da tela|
|`class`|nome de classe CSS|Aplica uma classe global a todos os slides|
|`backgroundColor`|cor (ex: `#fff` ou `black`)|Cor de fundo global|
|`color`|cor (ex: `#000`)|Cor do texto global|
|`header` / `footer`|texto ou markdown|Cabeçalho/rodapé fixo em todos os slides|
|`style`|bloco de CSS embutido|Define estilos personalizados inline|
|`math`|`mathjax` / `katex`|Ativa renderização de equações|
|`auto-scaling`|`true` / `false`|Ajusta o tamanho automático do texto|
|`title`|string|Título do documento|
|`description`|string|Descrição do documento|
|`transition`|`none`, `fade`, `slide`, `zoom`, etc.|(Alguns temas suportam) tipo de transição|
|`direction`|`horizontal` / `vertical`|Direção dos slides (nem todos os temas suportam)|

---

## 2. Estilização via `style:` (CSS embutido)

Dentro do front-matter, você pode adicionar:

```yaml
style: |
  section {
    background: #f0f0f0;
    color: #222;
  }

  section.lead {
    background: #002b36;
    color: #eee;
  }

  h1 {
    font-size: 2.4em;
    text-transform: uppercase;
  }

  img {
    border-radius: 16px;
    box-shadow: 0 0 12px rgba(0,0,0,0.3);
  }
```

---

## 3. Propriedades locais (por slide)

Essas são colocadas **acima do conteúdo de um slide**:

```markdown
<!-- _class: lead -->
<!-- _backgroundColor: #002b36 -->
<!-- _color: #fff -->
<!-- _backgroundImage: url('minha-imagem.png') -->
<!-- _paginate: false -->
```

 Essas opções só afetam o **slide atual**.

---

