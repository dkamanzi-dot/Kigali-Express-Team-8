# Pitch: WWDC June 2027

It's lunchtime in Kigali. 10,000 drivers are on the road, and a customer taps "Order".

Before, our app checked every driver one by one to find the right one. That's up to 10,000 checks for every order.

Now we store the drivers in a dictionary by their ID, so the app goes straight to the driver in one step:

```python
driver = drivers_by_id.get(driver_id)
```

- Lookup time went from about 0.6 ms to 0.0004 ms, around 1,700x faster.
- Building the dictionary takes about 3 ms, and it only happens once.
- Lookups stay fast as the number of drivers grows.

Kigali Express, by Team 8.
