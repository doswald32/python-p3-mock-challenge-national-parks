class NationalPark:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        if not hasattr(self, 'name') and isinstance(value, str) and len(value) >= 3:
            self._name = value
        else: 
            raise Exception("Name must be a string of at least 3 characters.")

    def trips(self):
        return [trip for trip in Trip.all if type(trip) == Trip and trip.national_park == self]
    
    def visitors(self):
        unique_visitors = []
        for trip in Trip.all:
            if type(trip.visitor) == Visitor and trip.visitor not in unique_visitors:
                unique_visitors.append(trip.visitor)
        return unique_visitors
    
    def total_visits(self):
        park_visits = 0
        for trip in Trip.all:
            if trip.national_park == self:
                park_visits += 1
        if park_visits == 0:
            return 0
        else: 
            return park_visits
    
    def best_visitor(self):
        visitor_trips = {}
        for trip in Trip.all:
            if trip.national_park == self:
                if trip.visitor not in visitor_trips:
                    visitor_trips[trip.visitor] += 1
        best_vis = max(visitor_trips, key=lambda key: visitor_trips[key])
        return best_vis


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._start_date = value
        else: 
            raise Exception("Start date must be a string of 7 characters or more.")
        
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._end_date = value
        else:
            raise Exception("End date must be a string of 7 characters or more.")

    @property 
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, value):
        if isinstance(value, Visitor):
            self._visitor = value
        else: 
            raise Exception("Visitor must be of type Visitor.")
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, value):
        if not hasattr(self, "national_park") and isinstance(value, NationalPark):
            self._national_park = value
        else: 
            raise Exception("National Park must be of type NationalPark.")

class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not hasattr(self, 'name') and isinstance(value, str) and len(value) >= 3:
            self._name = value
        else:
            raise Exception("Name must be a string of at least 3 characters.")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self and type(trip) == Trip]
    
    def national_parks(self):
        np_list = []
        for trip in Trip.all:
            if trip not in np_list and trip.visitor == self:
                np_list.append(trip.national_park)
        return np_list
    
    def total_visits_at_park(self, park):
        total_visits = 0
        for trip in Trip.all:
            if trip.visitor == self and trip.national_park == park:
                total_visits += 1
        if total_visits == 0:
            return 0
        else:
            return total_visits