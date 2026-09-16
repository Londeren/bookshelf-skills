# Улов фазы 1 — $100M Money Models (2025) (ярус 1), тип E: глоссарий

Группа `tier1-money-models`, слаг `money-models`, ярус 1. Якоря единиц этого файла проверяются по оригиналам в `tmp/hormozi/`, файл назван в поле `source` каждой единицы (первым словом) и в `anchor_at`.

Единиц в файле: **43** (экстрактор вернул 43, отброшено на механической проверке якорей: 0).

| файл | строки / символы | кусков чтения | единиц |
|---|---|---|---|
| `100m-money-models.md` | 1–6495 | 7 | 43 |

## Как собран файл

Экстрактор E (Glossary) — отдельный агент Opus 5, получил полный текст группы (очищенные копии с той же нумерацией строк, что в оригинале: служебные строки заменены пустыми, остальные не тронуты), затем задание по листу `01-extractors.md` book-to-skill и карте `pipeline/hormozi/BOOK_OVERVIEW.md`. Сначала выписал дословные пассажи, затем сформулировал единицы.

Блоки единиц перенесены из сырого выхода экстрактора **байт в байт**; поле `anchor` не перепечатывалось. Единственное добавленное поле — `anchor_at`: файл и строка (для транскриптов — файл и символьное смещение), где якорь механически найден в оригинале скриптом `.superpowers/hormozi/verify_anchors.py` (`str.find`, точная подстрока). Единица, чей якорь в оригинале не найден, в файл не попала и записана в `.superpowers/hormozi/reports/dropped-tier1-money-models.md`.

Проверить якоря этого файла: `python3 .superpowers/hormozi/verify_anchors.py pipeline/hormozi/catch/tier1-money-models-E.md` (нужны источники в `tmp/hormozi/`, в git их нет). Якорей, встречающихся в файле-источнике больше одного раза: 2; единиц, где строка в `source` расходится с `anchor_at` больше чем на 40 строк: 0 (адрес экстрактора сохранён, точное место даёт `anchor_at`).

## Как обращаться с якорем

`anchor` — дословная подстрока одной строки файла-источника, включая escape-последовательности Calibre (`\$`), спаны `[…]{.calibreN}`, HTML-сущности OCR, потерянные точки Lost Chapters и пробел перед точкой в плейбуках. Нормализовать и перепечатывать нельзя: проверка ведётся точным поиском подстроки.

```yaml
- id: E-money-models-001
  type: term
  name: >-
    Money Model
  statement: >-
    A Money Model is the deliberate sequence of offers a business makes to a customer — what you offer, when you offer it and how — not a single offer or a price list.
  definition: >-
    A Money Model is a sequence of offers. At their core, we find every opportunity to solve a customer's problem...and then offer to solve it. It's what you offer, when you offer, and how you offer it to make as much money as you can as fast as you can.
  not_to_confuse_with: >-
    A single offer: the author stresses that Money Models tend to have many offers in a specific order, and that if you offer the right thing when customers realize they need it, you can make as many offers as you like.
  anchor: >-
    A Money Model is *a deliberate sequence of offers*. It's what you offer,
  source: >-
    100m-money-models.md, Section VI: Make Your Money Model, Description, line 5823
  confirmations: 3
  anchor_at: "100m-money-models.md:5823"
- id: E-money-models-002
  type: term
  name: >-
    A good Money Model
  statement: >-
    A Money Model counts as good when one customer produces more profit in the first 30 days than it costs to get and service that same customer — the author's bare minimum, not a target.
  definition: >-
    A good Money Model makes more profit from a customer than it costs to get and service them in the first 30 days. That's the bare minimum.
  not_to_confuse_with: >-
    A $100M Money Model, which the author sets one level higher: profit from one customer above the cost of getting and servicing many.
  anchor: >-
    **A good Money Model** *makes more profit from a customer than it
  source: >-
    100m-money-models.md, Ten Years In Ten Minutes, What We Covered, line 6166
  confirmations: 1
  anchor_at: "100m-money-models.md:6166"
- id: E-money-models-003
  type: term
  name: >-
    $100M Money Model
  statement: >-
    A $100M Money Model makes more profit from one customer in the first 30 days than it costs to get and service many customers, which removes cash as the limit on growth.
  definition: >-
    A $100M Money Model makes more profit from one customer than it costs to get and service many customers in the first 30 days, which removes cash as a limiter to scaling your business.
  why: >-
    With so much money made in the first thirty days, the cost of getting more customers is never a problem again, and the business is forced to fix everything else just to keep up.
  anchor: >-
    **A \$100M Money Model** *makes more profit from one customer than
  source: >-
    100m-money-models.md, Ten Years In Ten Minutes, What We Covered, line 6171
  confirmations: 3
  anchor_at: "100m-money-models.md:6171"
- id: E-money-models-004
  type: term
  name: >-
    Attraction Offer
  statement: >-
    An Attraction Offer is the offer that turns strangers into customers by offering something free or at a discount, generating leads and converting them in one move.
  definition: >-
    Attraction Offers generate leads and convert them into customers. They turn advertising into money by offering something free or at a discount. Attraction Offers turn strangers into customers.
  not_to_confuse_with: >-
    A lead-generation offer alone: the author's Attraction Offer both generates the lead and converts it, and often also makes money by offering a better deal at a higher price.
  anchor: >-
    Attraction Offers generate leads *and* convert them into customers. They
  source: >-
    100m-money-models.md, Section II: Attraction Offers, line 1026
  confirmations: 3
  anchor_at: "100m-money-models.md:1026"
- id: E-money-models-005
  type: term
  name: >-
    free / discount / $1 (the discount continuum)
  statement: >-
    In this method free, discount and $1 are interchangeable labels on one continuum, so any play written with free can be run as a discount or a $1 price and the other way round.
  definition: >-
    Any time I say free you can also use discount or $1. Any time I use discount you can also use free or $1 and so on. They exist on a continuum because they all discount a product to some level — even if you discount it by 100%.
  why: >-
    Strangers can only take your word on value but they absolutely understand price, so discounts make anything a great deal to just about anyone; the greater the discount the better the deal, the greatest of all being free.
  anchor: >-
    So first off, any time I say "free" you can also use "discount" or
  source: >-
    100m-money-models.md, Section II: Attraction Offers, line 1035
  confirmations: 1
  anchor_at: "100m-money-models.md:1035"
- id: E-money-models-006
  type: term
  name: >-
    Win Your Money Back
  statement: >-
    Win Your Money Back is the Attraction Offer where the seller sets the customer's goal and the route to it, and the customer who reaches it qualifies for their money back in cash or store credit.
  definition: >-
    A Win Your Money Back Offer works like this. You set a goal for the customer and tell them how to reach it. If they reach it, then they qualify to get their money back or get it back as store credit. Bottom line: customers put money down. If they do the stuff OR they get the result OR both — they get it back as cash or store credit.
  not_to_confuse_with: >-
    Trial With Penalty, which the author separates himself: Win Your Money Back gives customers the chance to get their money back if they meet the terms; in Trial With Penalty customers only pay if they don't meet the terms.
  applies_when: >-
    Businesses that require their customers to put in continuous effort to get their ideal outcome, and stuff people start and quit.
  anchor: >-
    A Win Your Money Back Offer works like this. *You* set a goal for the
  source: >-
    100m-money-models.md, Win Your Money Back, Description, line 1139
  confirmations: 3
  authors_caveat: >-
    Only use a Win Your Money Back Offer if your refund rate is below 5%; and only offer it if you feel OK with giving money back, since about 10% of all customers will ask for it.
  anchor_at: "100m-money-models.md:1139"
- id: E-money-models-007
  type: term
  name: >-
    Giveaway Offer
  statement: >-
    A Giveaway Offer advertises a chance to win a big prize in exchange for contact information, and after a winner is picked everyone else is offered the same prize at a discount.
  definition: >-
    Giveaway Offers advertise a chance to win a big prize in exchange for contact information and whatever else you want. Then, after picking a winner, you offer everyone else the big prize at a discounted price.
  not_to_confuse_with: >-
    Scholarship, sweepstakes and raffle are the author's own aliases for the same offer: they all mean enter for a chance to win.
  anchor: >-
    Giveaway Offers advertise a chance to win a big prize in exchange for
  source: >-
    100m-money-models.md, Giveaways, Description, line 1513
  confirmations: 2
  anchor_at: "100m-money-models.md:1513"
- id: E-money-models-008
  type: term
  name: >-
    Grand Prize
  statement: >-
    The Grand Prize of a Giveaway is the thing you want everyone to buy, carrying an assigned monetary value that serves as the price anchor for the offer made to everyone who does not win.
  definition: >-
    Make your Grand Prize the thing you want everyone to buy. Make sure you assign a monetary value to your grand prize to serve as a price anchor.
  why: >-
    Leads entered because they found the Grand Prize interesting, so the bigger the value assigned to it, the more compelling the discounted offer made to everyone else.
  anchor: >-
    **Pick A Grand Prize.** Make your Grand Prize *the thing you want
  source: >-
    100m-money-models.md, Giveaways, Description, line 1535
  confirmations: 2
  anchor_at: "100m-money-models.md:1535"
- id: E-money-models-009
  type: term
  name: >-
    Promotional Offer (Giveaway)
  statement: >-
    The promotional offer is the discounted version of the Grand Prize that every non-winning entrant qualifies for — the author's generalisation of the partial scholarship.
  definition: >-
    Your promotional offer takes the place of the partial scholarship in the story. You create it by enhancing your core offer with a discount, a bonus, or by minorly changing it from the Grand Prize in order to ethically justify a price reduction (using the Grand Prize as a price anchor).
  not_to_confuse_with: >-
    The Grand Prize: the Grand Prize is announced publicly to one winner, while everybody else qualifies for the promotional offer, which the author calls a participation trophy.
  anchor: >-
    **Pick Your Promotional Offer.** Your promotional offer takes the place
  source: >-
    100m-money-models.md, Giveaways, Description, line 1540
  confirmations: 1
  anchor_at: "100m-money-models.md:1540"
- id: E-money-models-010
  type: term
  name: >-
    Qualifying Actions
  statement: >-
    Qualifying Actions are the things a Giveaway entrant must do to qualify to win, chosen so they also promote the giveaway or demonstrate a higher level of interest.
  definition: >-
    Other stuff entrants do to qualify to win. I also use these to get them to promote my giveaway more, or demonstrate higher levels of interest. Ex: attending a call or event, making a post, entering a group, etc.
  not_to_confuse_with: >-
    Eligibility, which the author keeps separate: eligibility questions ask whether the entrant is a fit for the product (Do you own a vet clinic? Why should you be selected?), while qualifying actions are things they do.
  anchor: >-
    **Qualifying Actions.** Other stuff entrants do to qualify to win. I
  source: >-
    100m-money-models.md, Giveaways, Description, line 1564
  confirmations: 1
  anchor_at: "100m-money-models.md:1564"
- id: E-money-models-011
  type: term
  name: >-
    Decoy Offer
  statement: >-
    A Decoy Offer advertises something free or discounted, and when leads engage both the decoy and a more valuable premium offer are presented side by side.
  definition: >-
    Decoy Offers advertise something free or discounted. Then, when leads ask to learn more, you also present a more valuable premium offer. The premium offer provides more features, benefits, bonuses, guarantees, and so on.
  why: >-
    By putting decoy and premium side by side leads see how much more valuable the premium is; either way you close everyone, which makes getting new customers cheap and profitable.
  not_to_confuse_with: >-
    The premium offer itself: the decoy is deliberately a lesser, smaller or simpler version of the premium offer, made by offering fewer components, older models, less personalisation and no guarantees.
  anchor: >-
    Decoy Offers advertise something free or discounted. Then, when leads
  source: >-
    100m-money-models.md, Decoy Offer, Description, line 1866
  confirmations: 3
  anchor_at: "100m-money-models.md:1866"
- id: E-money-models-012
  type: term
  name: >-
    Buy X Get Y Free
  statement: >-
    In a Buy X Get Y Free Offer the customer buys one thing and gets other things free, which reframes a discount as a free offer.
  definition: >-
    In Buy X Get Y Free Offers, when customers buy something, they get other stuff free. The more free stuff they get, and the higher its value, the better it works.
  why: >-
    Free offers get way more attention than Discount Offers, and selling more than one thing at once lets you make the discount large enough to cover the price of more stuff.
  applies_when: >-
    Stuff that makes sense to buy more of or get longer access to.
  anchor: >-
    In Buy X Get Y Free Offers, when customers buy something, they get other
  source: >-
    100m-money-models.md, Buy X Get Y Free, Description, line 2088
  confirmations: 3
  anchor_at: "100m-money-models.md:2088"
- id: E-money-models-013
  type: term
  name: >-
    Pay Less Now or Pay More Later
  statement: >-
    Pay Less Now or Pay More Later gives people a choice between paying full price later, only if satisfied, and paying a discounted price now with bonuses.
  definition: >-
    In Pay Less Now or Pay More Later, you give people a choice to pay full-price later OR pay a discounted price now. The pay now option offers a 20-50% discount and bonuses if they pay now.
  why: >-
    It removes all risk from the customer, combining a delayed payment with a satisfaction guarantee, and the pay later option lets you advertise free while still getting their card on file.
  not_to_confuse_with: >-
    Trial With Penalty: the author uses Pay Less Now or Pay More Later as a downsell for physical products or one-time services, and Trial With Penalty as a downsell for recurring products or services.
  anchor: >-
    In Pay Less Now or Pay More Later, you give people a choice to pay
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Description, line 2334
  confirmations: 3
  anchor_at: "100m-money-models.md:2334"
- id: E-money-models-014
  type: term
  name: >-
    Conditional Satisfaction Guarantee
  statement: >-
    A conditional satisfaction guarantee lets the customer cancel the billing only if they meet stated conditions, usually the actions that get them the most value from the product.
  definition: >-
    People can only cancel the billing if they qualify. So, be sure to track the conditions necessary to qualify. Think: attendance, showing up to an appointment, turning in data, etc. Make the criteria what people do to get the most value out of the product.
  why: >-
    They can't say you suck if they never try it.
  anchor: >-
    **Make a Conditional Satisfaction Guarantee.** *People can only cancel
  source: >-
    100m-money-models.md, Pay Less Now or Pay More Later, Important Notes, line 2415
  confirmations: 2
  anchor_at: "100m-money-models.md:2415"
- id: E-money-models-015
  type: term
  name: >-
    Upsell Offer
  statement: >-
    An upsell is simply whatever you offer next — more of what they just got, a better version, or something new and complementary — offered the moment the previous offer reveals the next problem.
  definition: >-
    Anytime you offer something next, you upsell. Upsells just mean whatever we offer next. When an offer solves a problem, another appears. You upsell the solution to the problem your offer reveals.
  why: >-
    The thing you sell the most isn't always the thing you make the most profit on; often upsells make the majority of the profit and make or break a Money Model.
  anchor: >-
    Anytime you offer something *next*, you upsell. Upsells play a key role
  source: >-
    100m-money-models.md, Upsell Offers Conclusion, line 3720
  confirmations: 3
  anchor_at: "100m-money-models.md:3720"
- id: E-money-models-016
  type: term
  name: >-
    The Classic Upsell
  statement: >-
    The Classic Upsell offers the solution to the customer's next problem the moment they become aware of it, in a You can't have X without Y structure.
  definition: >-
    The Classic Upsell offers a solution to the customer's next problem the moment they become aware of it. Your core offer solves one problem and creates another. Your upsell immediately solves that next problem. This gives the classic upsell its You can't have X without Y structure.
  why: >-
    Current customers always have a higher chance of buying your stuff than strangers, and when timed right customers upsell themselves.
  anchor: >-
    The Classic Upsell offers a solution to the customer's next problem *the
  source: >-
    100m-money-models.md, The Classic Upsell, Description, line 2754
  confirmations: 2
  anchor_at: "100m-money-models.md:2754"
- id: E-money-models-017
  type: term
  name: >-
    Say No To Say Yes
  statement: >-
    Say No To Say Yes is the author's name for closing with you don't want anything else do you? — the habitual no is in fact agreement to what was just offered.
  definition: >-
    People had been trained to say no in response to you don't want anything else do you? But this actually turns a no into yes. So when upselling, the question translates to: You don't want anything [besides what I just offered] do you?
  anchor: >-
    **Get Them To "Say No To Say Yes."** I was always amazed at how often
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2818
  confirmations: 3
  anchor_at: "100m-money-models.md:2818"
- id: E-money-models-018
  type: term
  name: >-
    Hyper Buying Cycle
  statement: >-
    The hyper buying cycle is the short window after a buyer decides to do something new, when they are most excited and spend a huge chunk of money in a short period.
  definition: >-
    Most buyers enter a hyper buying cycle when they decide to do something new. It's a short window of time when they are the most excited about a new thing they're gonna do. This is when they spend a huge chunk of money in a short period of time.
  applies_when: >-
    Businesses catering to weddings, starting new hobbies, having babies, moving to new places and similar decisions.
  anchor: >-
    enter a "hyper buying" cycle when they decide to do something new. It's
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2833
  confirmations: 1
  anchor_at: "100m-money-models.md:2833"
- id: E-money-models-019
  type: term
  name: >-
    BAMFAM
  statement: >-
    BAMFAM stands for Book-A-Meeting-From-A-Meeting: every appointment ends by scheduling the next one, so the customer knows the next time they see you and why before they leave.
  definition: >-
    Make sure you Book-A-Meeting-From-A-Meeting (BAMFAM). End every appointment by scheduling the next appointment. Don't let them leave without booking.
  why: >-
    The more times you can upsell, the more people you will upsell; if you upsell more people, you make more money.
  anchor: >-
    **Make Sure You Book-A-Meeting-From-A-Meeting (BAMFAM).** The more times
  source: >-
    100m-money-models.md, The Classic Upsell, Important Notes, line 2873
  confirmations: 2
  anchor_at: "100m-money-models.md:2873"
- id: E-money-models-020
  type: term
  name: >-
    Menu Upsell
  statement: >-
    In a Menu Upsell you first tell customers which options they don't need, then what they do need, then ask their preference, then settle payment on the card on file.
  definition: >-
    In a Menu Upsell, you tell customers which options they don't need. Then, tell them what they do need, their preferences, and how to get their value from it. Menu Upsells combine up to four tactics: Unselling, Prescription Upselling, A/B Upselling, and Card On File.
  applies_when: >-
    Menu Upsells work best when you have multiple offers available.
  anchor: >-
    In a Menu Upsell, you tell customers which options they don't need.
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3084
  confirmations: 3
  anchor_at: "100m-money-models.md:3084"
- id: E-money-models-021
  type: term
  name: >-
    Unselling
  statement: >-
    Unselling is telling customers what they don't need, crossing options out, so as to emphasise and excite them about what they do need.
  definition: >-
    You unsell by telling customers what they don't need so that you can emphasize what they do. Here, instead of asking if they want to buy it or not, you explain what they don't need as a way to get them excited about what they do.
  why: >-
    Going out of the way to cross out what the customer didn't need built enough goodwill to upsell what she did; unselling lower-margin stuff where appropriate incentivizes higher-margin upsells.
  anchor: >-
    *Unselling.* You unsell by telling customers what they don't need so
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3097
  confirmations: 3
  anchor_at: "100m-money-models.md:3097"
- id: E-money-models-022
  type: term
  name: >-
    Prescription Upsell
  statement: >-
    A Prescription Upsell tells the customer what they do need and exactly how to use it, as if they already own it, instead of asking whether they want it.
  definition: >-
    We tell them what they do need. Prescription upselling has two important components. First, you have to explain how it integrates with offers they already bought. Second, you personalize and detail how to maximize its value. Here, instead of asking if they want to buy it or not, you explain how to use it as if they already have.
  applies_when: >-
    Prescription Upsells work well when offering a choice is inconvenient and you have only one thing that solves the problem.
  why: >-
    Detailed and personalized instructions upsell more people than vague and general suggestions; removing the option of not buying lowers the chance they don't buy.
  anchor: >-
    *Prescription Upsell.* We tell them what they do need. Prescription
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3104
  confirmations: 2
  anchor_at: "100m-money-models.md:3104"
- id: E-money-models-023
  type: term
  name: >-
    A/B Upsell
  statement: >-
    An A/B Upsell asks which of two products the customer prefers rather than whether they want to buy at all, so either answer is a sale.
  definition: >-
    We ask them their preferences. A/B Upsells work for multiple offers that solve the same problem. Instead of asking if customers wanted to buy a product, yes or no, we ask which product they prefer: A or B. Either choice results in an upsell.
  why: >-
    When you give people the option to not buy, some don't buy; so the choice is between buying two similar things.
  anchor: >-
    *A/B Upsell.* We ask them their preferences. A/B Upsells work for
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3114
  confirmations: 3
  anchor_at: "100m-money-models.md:3114"
- id: E-money-models-024
  type: term
  name: >-
    Card On File
  statement: >-
    Card On File is closing payment with Do you want to use the card on file? — referring to a payment method the customer already gave instead of asking whether they want to pay.
  definition: >-
    I literally ask, Do you want to use the card on file? Here, instead of asking if they want to pay or not, you refer to ways they already have.
  why: >-
    It lowers the hidden costs of buying — picking which card, taking it out, being reminded of ugly buying decisions in the past — and if you make it easy for people to buy, more people will.
  anchor: >-
    Last, I make buying easy by asking if they want to use the card on file.
  source: >-
    100m-money-models.md, Menu Upsell, Description, line 3095
  confirmations: 3
  anchor_at: "100m-money-models.md:3095"
- id: E-money-models-025
  type: term
  name: >-
    Anchor Upsell
  statement: >-
    In an Anchor Upsell the premium thing is offered first, and when the customer balks a cheaper but acceptable alternative with the same core functions is presented.
  definition: >-
    With Anchor Upsells, you offer premium stuff first. If the customer gasps, you offer a cheaper but acceptable alternative. Present the Anchor, get The Gasp, come to the rescue, present your main offer, ask how they wanna pay.
  why: >-
    If you present a premium version that's 5x-10x the price first, the main offer then looks like a much better deal, anchored customers spend more than they normally would, and some customers still buy the super expensive thing.
  applies_when: >-
    Anchor Upsells work best when the lower-price offer has the same core functions as the premium one.
  anchor: >-
    With Anchor Upsells, you offer premium stuff first. If the customer
  source: >-
    100m-money-models.md, Anchor Upsell, Description, line 3333
  confirmations: 2
  authors_caveat: >-
    If you treat the anchor like a fake, so will the customer: the premium offer must be one you actually want people to buy and actually sell.
  anchor_at: "100m-money-models.md:3333"
- id: E-money-models-026
  type: term
  name: >-
    The Gasp
  statement: >-
    The Gasp is the customer's mini panic attack at the price of the anchor offer, and the signal to come to the rescue with the main offer.
  definition: >-
    When you do an anchor upsell correctly, customers will have mini panic attacks. I call this The Gasp. The bigger the gasp, the more they bought.
  why: >-
    If your customers don't gasp, then they probably find your premium offer reasonable — so just ask them if they wanna use the card on file.
  anchor: >-
    correctly, customers will have mini panic attacks. I call this "The
  source: >-
    100m-money-models.md, Anchor Upsell, Important Notes, line 3416
  confirmations: 2
  anchor_at: "100m-money-models.md:3416"
- id: E-money-models-027
  type: term
  name: >-
    Rollover Upsell
  statement: >-
    A Rollover Upsell credits some or all of a customer's previous purchases toward the next, more expensive offer.
  definition: >-
    Rollover Upsells credit some or all of a customer's previous purchases toward your next offer. Once I know how much credit to give, I figure out three things: who to upsell, what to upsell, and how to roll over the credit.
  applies_when: >-
    Four situations: to re-engage customers who left a while ago, to rescue upset customers as a better alternative to a refund, to rescue other people's upset customers, and to upsell regular customers.
  anchor: >-
    Rollover Upsells credit some or all of a customer's previous purchases
  source: >-
    100m-money-models.md, Rollover Upsell, Description, line 3558
  confirmations: 3
  authors_caveat: >-
    Price the next offer at least 4x higher than the credit, so that applying the whole amount discounts 25% at most and the offer still makes a profit.
  anchor_at: "100m-money-models.md:3558"
- id: E-money-models-028
  type: term
  name: >-
    Winback campaign
  statement: >-
    A winback campaign is a Rollover Upsell aimed at customers 6+ months since their last purchase, offering them credit from what they paid before to return.
  definition: >-
    Reach out to old customers (6+ months since last purchase). Look at how much they paid before. Decide how much you're willing to roll over. Offer it. I called these winback campaigns.
  anchor: >-
    Actually do this. I called these "winback campaigns." I made
  source: >-
    100m-money-models.md, Rollover Upsell, Important Notes, line 3647
  confirmations: 2
  anchor_at: "100m-money-models.md:3647"
- id: E-money-models-029
  type: term
  name: >-
    Downsell
  statement: >-
    A downsell is any offer made after someone says no: the original offer tweaked to find the highest value solution for that customer's budget, by changing how they pay or what they get.
  definition: >-
    Downselling tweaks the original offer to find the highest value solution for the customer's budget. So any offer you make after someone says no is a downsell. I downsell in two ways. I change how they pay or what they get.
  not_to_confuse_with: >-
    Discounting, which the author separates explicitly: dropping your price is not really downselling, it's discounting — the offer is never the same stuff for cheaper.
  anchor: >-
    Downselling tweaks the original offer to find the highest value solution
  source: >-
    100m-money-models.md, Section IV: Downsell Offers, line 3747
  confirmations: 3
  anchor_at: "100m-money-models.md:3747"
- id: E-money-models-030
  type: term
  name: >-
    Payment Plan Downsell
  statement: >-
    A Payment Plan Downsell offers the same product at the same price, spreading the cost by charging some of it up front and putting the rest into scheduled payments.
  definition: >-
    Payment Plan Downsells spread the cost of a product by charging some of it up front and putting the rest into scheduled payments.
  why: >-
    A huge percentage of the time it costs too much really means this costs too much up front; payment plans get more buyers because customers pay less in the moment but still pay full price over time.
  anchor: >-
    ● Payment Plan Downsells spread the cost of a product by charging some
  source: >-
    100m-money-models.md, Payment Plan Downsells, Summary Points, line 4092
  confirmations: 3
  authors_caveat: >-
    Payment plans only grow the business if they get more customers and those customers actually pay; you want to close more appointments overall but with the same percentage of appointments paying in full.
  anchor_at: "100m-money-models.md:4092"
- id: E-money-models-031
  type: term
  name: >-
    Seesaw Downselling
  statement: >-
    Seesaw Downselling is the short form of the payment plan process: it gradually shifts from paid-in-full to equal payments by adjusting the down payment until the monthly rate is acceptable.
  definition: >-
    Seesaw Downselling gradually shifts from paid-in-full to equal payments. Instead of asking for the full amount, just ask Would you rather have giant monthly payments or tiny ones? Then the more they put down now, the lower their monthly payments.
  applies_when: >-
    If you prefer fewer steps, or have less experienced salespeople.
  anchor: >-
    ● "Seesaw" Downselling gradually shifts from paid-in-full to equal
  source: >-
    100m-money-models.md, Payment Plan Downsells, Summary Points, line 4126
  confirmations: 2
  anchor_at: "100m-money-models.md:4126"
- id: E-money-models-032
  type: term
  name: >-
    Trial With Penalty
  statement: >-
    In a Trial With Penalty the customer gets the product free so long as they meet stated terms, and pays a fee only where they fail to meet them.
  definition: >-
    In a Trial With Penalty offer, customers can try your product or service for free so long as they meet your terms. Customers only pay if they don't meet the terms.
  not_to_confuse_with: >-
    Win Your Money Back, which pays money back if the customer meets the terms, and an ordinary free trial: Trial With Penalty isn't here's my thing, see if you like it — it's here's my thing, you get it for free so long as you do this stuff, and if you don't, then you have to pay for it.
  applies_when: >-
    As a downsell for recurring products or services, and only in businesses where the customer has to do work to get results.
  anchor: >-
    In a Trial With Penalty offer, customers can try your product or service
  source: >-
    100m-money-models.md, Trial With Penalty, Description, line 4203
  confirmations: 3
  authors_caveat: >-
    Customer-facing, just call it a Free Trial: people may get scared and confused otherwise, since no one wants to be penalized.
  anchor_at: "100m-money-models.md:4203"
- id: E-money-models-033
  type: term
  name: >-
    Feature Downsell
  statement: >-
    A Feature Downsell lowers the price by changing what the customer gets — less quantity, lower quality, a cheaper alternative, or cutting optional components.
  definition: >-
    Feature Downsells lower prices by changing what customers get. I do them by offering lesser quantity, lower quality, lower price alternatives, or cutting optional components. Take something away, lower the price, and in so many words ask how about now?
  not_to_confuse_with: >-
    A discount, which makes the same stuff cheaper; a Feature Downsell lowers the price by changing what they get.
  why: >-
    People see the value in what you removed after they see the price difference, so removing features from highest to lowest value gets customers to re-upsell themselves onto the more expensive offer.
  anchor: >-
    Feature Downsells lower prices by changing what customers get. I do them
  source: >-
    100m-money-models.md, Feature Downsells, Description, line 4559
  confirmations: 3
  anchor_at: "100m-money-models.md:4559"
- id: E-money-models-034
  type: term
  name: >-
    DIY, DWY, DFY
  statement: >-
    DIY, DWY and DFY name the service-delivery levels — Do It Yourself, Done With You, Done For You — and are one of the quality dials a Feature Downsell moves.
  definition: >-
    DIY, DWY, DFY. Do It Yourself vs. Done With You vs. Done For You.
  applies_when: >-
    Feature downselling service quality; if someone says no to all your service downsells, you can downsell another product that solves the same problem, moving Done-For-You to Do-It-Yourself.
  anchor: >-
    ● DIY, DWY, DFY. Do It Yourself vs. Done With You vs.
  source: >-
    100m-money-models.md, Feature Downsells, Feature Downsell Examples, line 4633
  confirmations: 2
  anchor_at: "100m-money-models.md:4633"
- id: E-money-models-035
  type: term
  name: >-
    Business terrorists
  statement: >-
    Business terrorists are people who demand to pay less for the same thing, and the author does not negotiate with them.
  definition: >-
    People who demand to pay less for the same thing are business terrorists. I don't negotiate with terrorists. If they want to pay less now — offer a payment plan. If they want to pay less overall — offer a feature downsell.
  anchor: >-
    **Remember, Never Negotiate The Price.** People who demand to pay less
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4679
  confirmations: 1
  anchor_at: "100m-money-models.md:4679"
- id: E-money-models-036
  type: term
  name: >-
    The Minimum
  statement: >-
    The Minimum is the author's name for the cheapest named feature combination, chosen because the word implies the customer has to take at least that much.
  definition: >-
    I name my cheapest combination The Minimum. I like it because it implies they have to get at least that thing. If someone rejects all other packages, I just say so nothing more than the minimum package then? to get them to say no to say yes.
  not_to_confuse_with: >-
    The most expensive combination, which is named after an aspirational status — The Whale Package, The Total Transformation, High Roller.
  anchor: >-
    **I Name My Cheapest Combination "The Minimum."** I like it because it
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4714
  confirmations: 2
  anchor_at: "100m-money-models.md:4714"
- id: E-money-models-037
  type: term
  name: >-
    Temperature Check
  statement: >-
    A Temperature Check is the pause after two refused changes in which you ask, on a scale from 1-10, how badly the person wants the thing, before continuing to downsell.
  definition: >-
    If you make two changes in a row and they still refuse, make sure they really want the thing. I'd say something like Got it. Real quick. I want to make sure. On a scale from 1-10 how bad do you want this?
  why: >-
    No payment plan will satisfy a customer who doesn't want the thing, so make sure the person actually wants it before putting more effort into selling it.
  anchor: >-
    **Temperature Check After Two Downsells (Like Payment Plans).** If you
  source: >-
    100m-money-models.md, Feature Downsells, Important Notes, line 4719
  confirmations: 2
  anchor_at: "100m-money-models.md:4719"
- id: E-money-models-038
  type: term
  name: >-
    Continuity Offer
  statement: >-
    A Continuity Offer provides ongoing value that customers make ongoing payments for until they cancel, so you sell once and get paid again and again.
  definition: >-
    Continuity Offers provide ongoing value that customers make ongoing payments for — until they cancel. They boost the profit from every customer and give you one last thing to sell.
  not_to_confuse_with: >-
    A payment plan: the author separates them himself — it's silly for someone to pay for a one-day workshop forever; it makes sense for them to pay until they cover the cost, and that makes it a payment plan.
  why: >-
    On their own Continuity Offers attract more customers but leave you strapped for cash today, which is why the author makes them last, after Attraction, Upsell and Downsell Offers.
  anchor: >-
    Continuity Offers *provide ongoing value that customers make ongoing
  source: >-
    100m-money-models.md, Continuity Offers Conclusion, line 5721
  confirmations: 4
  anchor_at: "100m-money-models.md:5721"
- id: E-money-models-039
  type: term
  name: >-
    Continuity Bonus Offer
  statement: >-
    With a Continuity Bonus you give the customer an awesome thing if they sign up today, where the bonus itself typically has more value than the first continuity payment.
  definition: >-
    With Continuity Bonuses you give the customer an awesome thing if they sign up today. Typically, the bonus itself has more value than the first continuity payment. That's all there is to it.
  why: >-
    Join my membership program isn't nearly as compelling as get this free valuable thing, so you advertise the bonus and explain the rest after they show interest.
  anchor: >-
    With Continuity Bonuses you give the customer an awesome thing *if* they
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Description, line 4991
  confirmations: 3
  authors_caveat: >-
    Keep bonuses related to the core offer, or you attract the wrong customers; and use realistic bonus pricing, since made-up values won't anchor and lose trust.
  anchor_at: "100m-money-models.md:4991"
- id: E-money-models-040
  type: term
  name: >-
    Bonus (vs Discount)
  statement: >-
    In this method a bonus adds value while a discount lowers cost; both are used together because each works on the buying decision in its own way.
  definition: >-
    Bonus — adding value. For products, you can give away many small things or one big product that complements the subscription. Discount — lowering costs. Free stuff and discounts both affect how we make decisions. So, we want to do both to get the benefits of both.
  not_to_confuse_with: >-
    Each other: the author converts one into the other at will — Free Bonus: become a member for $200 then you get this $1,000 program as a free bonus; Steep Discount: get the $1,000 program for $1 if you become a member for $200.
  anchor: >-
    *Bonus*---*adding value.* For products, you can give away many small
  source: >-
    100m-money-models.md, Continuity Bonus Offers, Description, line 4995
  confirmations: 2
  anchor_at: "100m-money-models.md:4995"
- id: E-money-models-041
  type: term
  name: >-
    Continuity Discount Offer
  statement: >-
    A Continuity Discount Offer gives products or services away free — now or later — if the customer commits to buying more over time.
  definition: >-
    To make a one-time continuity discount, you give products or services away for free if the customer commits to buying more products and services over time. Continuity Discount Offers give continuity time for free if the customer signs up today.
  not_to_confuse_with: >-
    Buy X Get Y Free: the author says this looks like Buy X Get Y Free done continuity-style and that you'd be right, but there are enough differences specific to continuity that it justified its own chapter.
  applies_when: >-
    You know two things: how you'll apply the discount (up front, at the end, an even spread, or after the first month or two) and your cancellation policy.
  anchor: >-
    To make a one-time continuity discount, you give products or services
  source: >-
    100m-money-models.md, Continuity Discount Offers, Description, line 5314
  confirmations: 3
  anchor_at: "100m-money-models.md:5314"
- id: E-money-models-042
  type: term
  name: >-
    Lifetime Discount
  statement: >-
    A lifetime discount is a permanently lower rate the customer earns by staying past a set point, which the author puts at the month of greatest churn.
  definition: >-
    You advertise the lifetime discount. But, you make customers earn it. They get a lower rate if they stay past X period. Make X the month your average customer drops off.
  why: >-
    Allowing customers to earn a lifetime discount at your month of greatest churn encourages customers to stick through it for a lifetime lower rate.
  anchor: >-
    **Try Lifetime Discount At Your Most Common Churn Point.** You advertise
  source: >-
    100m-money-models.md, Continuity Discount Offers, Important Notes, line 5439
  confirmations: 3
  anchor_at: "100m-money-models.md:5439"
- id: E-money-models-043
  type: term
  name: >-
    Waived Fee Offer
  statement: >-
    A Waived Fee Offer presents a month-to-month option carrying a startup fee of 3-5x the monthly rate, and waives that fee entirely if the customer commits long term — with the fee payable if they cancel inside the term.
  definition: >-
    Waived Fee Offers work like this. First, you ask the customer to pay a startup fee as part of joining a month-to-month program. Typically, I do 3-5x my monthly rate. Then, you offer to discount the entire fee if they commit longer term. But, if they cancel inside the term, they pay the fee.
  why: >-
    Customers will stay longer if leaving costs more than staying: fees get them to start because committing immediately avoids a fee, and fees get them to stick for the same reason.
  applies_when: >-
    Commitments of one year and longer; it works especially well with services that take a long time to work.
  anchor: >-
    Waived Fee Offers work like this. First, you ask the customer to pay a
  source: >-
    100m-money-models.md, Waived Fee Offer, Description, line 5594
  confirmations: 3
  authors_caveat: >-
    If more than 5% of people want to cancel early, look into it: pricing incentivizes sticking but it can't and shouldn't overcome a terrible product.
  anchor_at: "100m-money-models.md:5594"
```
