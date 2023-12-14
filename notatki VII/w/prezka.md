---
theme: Warsaw
aspectratio: 169
lang: pl 
section-titles: false
---

# Wstęp

Nowe rozwiązania przynoszą nowe zagrożenia, na które musimy uważać. Omówmy 
sobie parę z nich.

# Rodzaje zagrożeń

## Prompt Injection

::: { .columns align=center }

:::: column

- User input może nadpisać nasze instrukcje
- Często wymaga jakiejś specjalnej instrukcji dla modelu
- Proces jailbrakeów został już zautomatyzowany za pomocą LLM

::::

:::: column

![](./promptinjection.jpg)

::::

:::

## Nieprzewidywalność

::: { .columns align=center }

:::: { .column width=60% } 

- Nigdy nie wiemy jak zachowa się model
- Dane na których był trenowany mają wpływ na jego output
- Nie możemy polegać na modelach na dawanie outputu w określonej formie

::::

:::: { .column width=40% } 

![](./sd.png)

::::

:::

## Wycieki danych

::: { .columns align=center }

:::: { .column width=60% } 

- Zewnętrzne modele wiążą się z przesyłaniem przez api tajnych informacji
- Nawet jeśli posiadamy własny model, to jeśli miał w szkoleniu dostęp do
  danych poufnych to musimy zakładać że kiedyś je zwróci.

::::

:::: { .column width=40% } 

![](./samsung.png){height=80%}

::::

:::

## Koszta

::: { .columns align=center }

:::: { .column width=60% } 

- Modele są drogie w użyciu, a jednocześnie dość generyczne.
- Ich koszt zależy od wielkości kontekstu.

::::

:::: { .column width=40% } 

![](./localllama.png){height=80%}

::::

:::

# Podsumowanie

- LLM jako nowinka technologiczna jest przydatnym, lecz niebezpiecznym 
  narzędziem.
- LLM znakomicie nadaje się do tworzenia ataków na LLM
