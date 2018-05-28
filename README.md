# pingle

PiNGLE: The Piston Natural Grounded Language Environment

pingle is a python library intended to facilitate scientific
investigation into the intersection of natural language and
reinforcement learning. It inherits much of its design from OpenAI
Gym.

In the future, we hope to hook up pingle to many games in the Piston
project.

## Concepts

* Game: the term game is used with both its common English meaning and
  its mathematical definition from the field of game theory.

* Action: an action is a move or action taken within a game according
  to the rules of the game that has consequences specified by the
  rules of the game.

* Speech Act: a speech act is a series of signs that players of a game
  or external observers might choose to emit or not emit. pingle is
  currently focused on the domain of textual natural language, i.e.,
  strings containing natural language. Note that speech acts are not
  actions, because they have no effect on the outcome or conduct of
  the game as of yet. Future versions of pingle may make this
  distinction more fuzzy.

* Strategy: a strategy is a way that one might choose to play a
  particular game. In general, strategies are specific to individual
  games.

* Persona: a persona is a way that one might feel about the events of
  a game, or that one might pretend to feel. Personas are basically
  the same as strategies, except that they govern the use of speech
  acts rather than normal actions.

* Policy: a policy is a way that one might choose to fulfill a
  particular strategy or persona. This includes learned policies that
  are learned using reinforcement learning and other such techniques.

* The Extended Event Loop: we modify the standard reinforcement
  learning event loop to accomodate speech acts. Consider the gym
  event loop:

  ``obs, reward, done, info = env.step(action)``

  We propose to augment this with two speech acts: one that is taken
  after the observation is seen, that reflects upon the observation
  and all previous history, and another one that is taken after the
  action is selected, that reflects upon the action selected and all
  previous history.