/* PTS-BR: melhorias de leitura do site. O texto da especificação não muda; o script apenas
   aplica classes e estrutura. Sem o script, a página continua completa. */
(function () {
  "use strict";

  var ICONE_X = '<svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6 6 18"/><path d="m6 6 12 12"/></svg>';
  var ICONE_V = '<svg aria-hidden="true" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>';
  var ICONE_LUPA = '<svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>';

  function norm(s) {
    return String(s || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase().trim();
  }

  /* Rótulo em negrito no início de um parágrafo: "**Não aprovado:** ..." */
  function rotuloInicial(p) {
    var primeiro = p.firstChild;
    while (primeiro && primeiro.nodeType === 3 && !primeiro.textContent.trim()) {
      primeiro = primeiro.nextSibling;
    }
    if (!primeiro || primeiro.nodeName !== "STRONG") return null;
    return { el: primeiro, texto: primeiro.textContent.trim() };
  }

  function tirarRotulo(p, rotulo) {
    var depois = rotulo.el.nextSibling;
    rotulo.el.remove();
    if (depois && depois.nodeType === 3) depois.textContent = depois.textContent.replace(/^\s+/, "");
  }

  /* ---------- Avisos ---------- */
  var NIVEIS = { "PERIGO:": "perigo", "ATENÇÃO:": "atencao", "CUIDADO:": "cuidado", "NOTA:": "nota" };

  function avisos(raiz) {
    raiz.querySelectorAll("p").forEach(function (p) {
      var r = rotuloInicial(p);
      if (!r || !NIVEIS[r.texto] || p.classList.contains("pts-aviso")) return;
      p.classList.add("pts-aviso", "pts-aviso--" + NIVEIS[r.texto]);
      r.el.classList.add("pts-aviso__titulo");
      r.el.textContent = r.texto.replace(/:$/, "");
      var pai = p.parentElement;
      if (pai && pai.tagName === "BLOCKQUOTE" && pai.children.length === 1) pai.classList.add("pts-aviso-bloco");
    });
  }

  /* ---------- Comparação Não aprovado / PTS-BR ---------- */
  var LADOS = { "Não aprovado:": "nao", "PTS-BR:": "sim", "Aprovado:": "sim" };
  var CONTEUDO = /^(BLOCKQUOTE|OL|UL|PRE|TABLE)$/;

  function bloco(p, lado, rotulo) {
    var caixa = document.createElement("div");
    caixa.className = "pts-par__" + lado;
    var cab = document.createElement("p");
    cab.className = "pts-par__rotulo";
    cab.innerHTML = (lado === "nao" ? ICONE_X : ICONE_V) + rotulo.texto.replace(/:$/, "");
    p.parentNode.insertBefore(caixa, p);
    caixa.appendChild(cab);
    tirarRotulo(p, rotulo);
    if (p.textContent.trim() || p.querySelector("img,code")) caixa.appendChild(p);
    else p.remove();
    var prox = caixa.nextElementSibling;
    while (prox && (CONTEUDO.test(prox.tagName) || prox.classList.contains("highlight") || prox.classList.contains("md-typeset__scrollwrap"))) {
      var seguinte = prox.nextElementSibling;
      caixa.appendChild(prox);
      prox = seguinte;
    }
    return caixa;
  }

  function comparacoes(raiz) {
    var blocos = [];
    raiz.querySelectorAll("p").forEach(function (p) {
      if (p.closest(".pts-par__nao, .pts-par__sim, .pts-home")) return;
      var r = rotuloInicial(p);
      if (!r || !LADOS[r.texto]) return;
      blocos.push(bloco(p, LADOS[r.texto], r));
    });
    blocos.forEach(function (b) {
      if (!b.classList.contains("pts-par__nao") || b.parentElement.classList.contains("pts-par")) return;
      var par = document.createElement("div");
      par.className = "pts-par";
      b.parentNode.insertBefore(par, b);
      par.appendChild(b);
      var prox = par.nextElementSibling;
      if (prox && prox.classList.contains("pts-par__sim")) par.appendChild(prox);
    });
  }

  /* ---------- Regras (02) ---------- */
  var SELOS = { vale: "Linter e revisor", revisor: "Revisor" };

  function regras(raiz) {
    raiz.querySelectorAll("h3[data-verif]").forEach(function (h) {
      if (h.parentElement.classList.contains("pts-regra")) return;
      var texto = h.firstChild;
      if (texto && texto.nodeType === 3) {
        var m = texto.textContent.match(/^\s*(R\d+\.\d+)\s+/);
        if (m) {
          texto.textContent = texto.textContent.slice(m[0].length);
          var id = document.createElement("span");
          id.className = "pts-id";
          id.textContent = m[1];
          h.insertBefore(id, texto);
          var alias = document.createElement("span");
          alias.id = m[1].toLowerCase();
          h.insertBefore(alias, id);
        }
      }
      var selo = document.createElement("span");
      selo.className = "pts-selo";
      selo.textContent = "Verificação: " + (SELOS[h.getAttribute("data-verif")] || h.getAttribute("data-verif"));
      var link = h.querySelector(".headerlink");
      h.insertBefore(selo, link);

      var sec = document.createElement("section");
      sec.className = "pts-regra";
      h.parentNode.insertBefore(sec, h);
      var el = h;
      while (el && !(el !== h && /^H[123]$/.test(el.tagName)) && el.tagName !== "HR") {
        var seguinte = el.nextElementSibling;
        sec.appendChild(el);
        el = seguinte;
      }
    });
    raiz.querySelectorAll(".pts-regra > p").forEach(function (p) {
      var r = rotuloInicial(p);
      if (!r || !/^(Enunciado|Justificativa|Verificação|Exceção):$/.test(r.texto)) return;
      r.el.classList.add("pts-campo__rotulo");
      r.el.textContent = r.texto.replace(/:$/, "");
      p.classList.add("pts-campo");
    });
    if (/^#r\d+\.\d+$/.test(location.hash)) {
      var alvo = document.getElementById(location.hash.slice(1));
      if (alvo) alvo.parentElement.scrollIntoView();
    }
  }

  /* ---------- Dicionário (03) ---------- */
  var CABECALHO = ["Palavra (classe)", "Decisão", "Significado aprovado / Alternativa", "Exemplo PTS-BR", "Não aprovado"];
  var ALT = /([A-ZÀ-Ý][A-ZÀ-Ý-]*(?: [A-ZÀ-Ý][A-ZÀ-Ý-]*)*) \((v|s|adj|adv|prep|conj|pron|art|num|loc|abrev)\)/g;

  function dicionario(raiz) {
    var tabelas = Array.prototype.filter.call(raiz.querySelectorAll("table"), function (t) {
      var ths = Array.prototype.map.call(t.querySelectorAll("thead th"), function (th) { return th.textContent.trim(); });
      return ths.join("|") === CABECALHO.join("|");
    });
    if (!tabelas.length || raiz.querySelector(".pts-dic-busca")) return;

    var linhas = [];
    tabelas.forEach(function (t) {
      var wrap = t.closest(".md-typeset__scrollwrap") || t.parentElement;
      wrap.classList.add("pts-dic-wrap");
      var titulo = wrap.previousElementSibling;
      t.querySelectorAll("tbody tr").forEach(function (tr) {
        var tds = tr.children;
        for (var i = 0; i < tds.length; i++) tds[i].setAttribute("data-rotulo", CABECALHO[i] || "");
        var dec = tds[1].textContent.trim();
        var tipo = dec === "Aprovada" ? "a" : (dec === "Não aprovada" ? "n" : "o");
        var selo = document.createElement("span");
        selo.className = "pts-dec pts-dec--" + tipo;
        selo.textContent = dec;
        tds[1].replaceChildren(selo);
        if (tipo !== "a" && /^Use:/.test(tds[2].textContent.trim())) {
          tds[2].innerHTML = tds[2].innerHTML.replace(ALT, function (_, palavra, classe) {
            return '<button type="button" class="pts-alt" data-q="' + palavra.toLowerCase() + '">' + palavra + "</button> (" + classe + ")";
          });
        }
        linhas.push({
          tr: tr,
          tipo: tipo,
          palavra: norm(tds[0].textContent.replace(/\([^)]*\)\s*$/, "")),
          texto: norm(tds[0].textContent + " " + tds[2].textContent),
          wrap: wrap,
          titulo: titulo
        });
      });
    });

    var nA = linhas.filter(function (l) { return l.tipo === "a"; }).length;
    var nN = linhas.filter(function (l) { return l.tipo === "n"; }).length;
    var painel = document.createElement("div");
    painel.className = "pts-dic-busca";
    painel.innerHTML =
      '<label for="pts-dic-q">Buscar uma palavra</label>' +
      '<div class="pts-dic-campo">' + ICONE_LUPA +
      '<input id="pts-dic-q" type="search" autocomplete="off" placeholder="Por exemplo: excluir, rodar, consumo"></div>' +
      '<p class="pts-dic-ajuda">A busca encontra a palavra, o significado e a alternativa. Uma busca por "excluir" mostra EXCLUIR e as palavras não aprovadas que têm EXCLUIR como alternativa.</p>' +
      '<div class="pts-dic-filtros" role="group" aria-labelledby="pts-dic-rotulo"><span id="pts-dic-rotulo" class="pts-dic-rotulo">Decisão</span>' +
      '<button type="button" data-dec="todas" aria-pressed="true">Todas <span>' + linhas.length + "</span></button>" +
      '<button type="button" data-dec="a" aria-pressed="false">Aprovadas <span>' + nA + "</span></button>" +
      '<button type="button" data-dec="n" aria-pressed="false">Não aprovadas <span>' + nN + "</span></button></div>" +
      '<div class="pts-dic-resumo"><p aria-live="polite"></p><button type="button" class="pts-dic-limpar" hidden>Limpar a busca e o filtro</button></div>' +
      '<p class="pts-dic-vazio" hidden>Nenhuma palavra encontrada. Verifique a grafia. Se nenhuma palavra aprovada tiver o significado correto, envie um PMD (parte 05, seção 7).</p>';
    var primeiroTitulo = linhas[0].titulo;
    var ancora = raiz.querySelector("h2") || primeiroTitulo;
    ancora.parentNode.insertBefore(painel, ancora);
    var intro = [];
    for (var el = painel.nextElementSibling; el && el !== primeiroTitulo; el = el.nextElementSibling) intro.push(el);

    var campo = painel.querySelector("input");
    var resumo = painel.querySelector(".pts-dic-resumo p");
    var limpar = painel.querySelector(".pts-dic-limpar");
    var vazio = painel.querySelector(".pts-dic-vazio");
    var estado = { q: "", dec: "todas" };

    function aplicar() {
      var q = norm(estado.q);
      var visiveis = 0;
      var porWrap = new Map();
      linhas.forEach(function (l) {
        var ok = (estado.dec === "todas" || l.tipo === estado.dec) &&
          (!q || l.palavra.indexOf(q) === 0 || l.texto.indexOf(q) >= 0);
        l.tr.hidden = !ok;
        if (ok) visiveis++;
        porWrap.set(l.wrap, (porWrap.get(l.wrap) || 0) + (ok ? 1 : 0));
      });
      linhas.forEach(function (l) {
        var mostra = porWrap.get(l.wrap) > 0;
        l.wrap.classList.toggle("pts-dic-oculto", !mostra);
        if (l.titulo && /^H2$/.test(l.titulo.tagName)) l.titulo.classList.toggle("pts-dic-oculto", !mostra);
      });
      painel.querySelectorAll(".pts-dic-filtros button").forEach(function (b) {
        b.setAttribute("aria-pressed", String(b.getAttribute("data-dec") === estado.dec));
      });
      var filtrando = !!(q || estado.dec !== "todas");
      intro.forEach(function (el) { el.classList.toggle("pts-dic-oculto", filtrando); });
      resumo.textContent = filtrando
        ? (visiveis === 0 ? "Nenhuma entrada." : (visiveis === 1 ? "1 entrada" : visiveis + " entradas"))
        : linhas.length + " entradas";
      limpar.hidden = !filtrando;
      vazio.hidden = visiveis !== 0;
      var url = new URL(location.href);
      if (estado.q) url.searchParams.set("palavra", estado.q); else url.searchParams.delete("palavra");
      history.replaceState(null, "", url);
    }

    var espera;
    campo.addEventListener("input", function () {
      clearTimeout(espera);
      espera = setTimeout(function () { estado.q = campo.value; aplicar(); }, 120);
    });
    painel.querySelector(".pts-dic-filtros").addEventListener("click", function (ev) {
      var b = ev.target.closest("button[data-dec]");
      if (!b) return;
      estado.dec = b.getAttribute("data-dec");
      aplicar();
    });
    limpar.addEventListener("click", function () {
      estado = { q: "", dec: "todas" };
      campo.value = "";
      aplicar();
      campo.focus();
    });
    raiz.addEventListener("click", function (ev) {
      var b = ev.target.closest(".pts-alt");
      if (!b) return;
      estado = { q: b.getAttribute("data-q"), dec: "todas" };
      campo.value = estado.q;
      aplicar();
      painel.scrollIntoView({ block: "start" });
      campo.focus({ preventScroll: true });
    });

    var inicial = new URL(location.href).searchParams.get("palavra");
    if (inicial) { estado.q = inicial; campo.value = inicial; }
    aplicar();
  }

  function iniciar() {
    var raiz = document.querySelector(".md-content .md-typeset");
    if (!raiz) return;
    regras(raiz);
    comparacoes(raiz);
    avisos(raiz);
    dicionario(raiz);
  }

  if (window.document$ && typeof window.document$.subscribe === "function") {
    window.document$.subscribe(iniciar);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", iniciar);
  } else {
    iniciar();
  }
})();
