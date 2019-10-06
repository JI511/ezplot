# ----------------------------------------------------------------------------------------------------------------------
# Application
# ----------------------------------------------------------------------------------------------------------------------

# imports
import random
import datetime
from quicksqlite import Connection
import plot_date_data


class Application(object):
    """
    The application class.
    """
    def __init__(self):
        """
        Setup for the application class
        """
        self.table = 'Body_weight'
        self.database = 'Database.db'

    def run(self):
        """
        Runs the application.
        """
        # print(datetime.datetime.now())
        # self.setup_database()
        weights = self.get_database_values('Weight')
        dates = self.get_database_values('Date')
        plot_date_data.create_date_plot(x_data=dates, y_data=weights, title='Body Weight Change', x_label='Date',
                                        y_label='Body Weight')

    def setup_database(self):
        """
        Sets up initial database.
        """
        con = Connection(path=self.database, auto_commit=False, reconnects=5, auto_connect=True)
        con.create_table(self.table, ['Weight', 'date'], ['INTEGER', 'TEXT'])
        for i in range(11, 25):
            con.insert(self.table, [random.randint(100, 300), '2019-%s-06 16:13:54.511619' % i])
        con.commit()
        print(con.select(self.table, ["Weight", "date"], fetchall=True))
        con.close()

    def get_database_values(self, column_name):
        """
        Gets all values for a database column.

        :param str column_name:
        :return: Values from the database column.
        :rtype: list
        """
        con = Connection(path=self.database, auto_commit=False, reconnects=5, auto_connect=True)
        db_ret = con.select(self.table, column_name, fetchall=True)
        con.close()
        return [a[0] for a in db_ret]


# ----------------------------------------------------------------------------------------------------------------------
# End
# ----------------------------------------------------------------------------------------------------------------------
