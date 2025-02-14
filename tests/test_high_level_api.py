def variable(data, units, standard_name):
    return (["z",], data, {"units": units, "standard_name": standard_name})

def create_circ_xarray_dataset():
    from xarray import Dataset
    temperature = [288.99,]
    pressure = [98388.,]
    xh2o = [0.006637074,]
    xco2 = [0.0003599889,]
    xo3 = [6.859128e-08,]
    xn2o = [3.199949e-07,]
    xco = [1.482969e-07,]
    xch4 = [1.700002e-06,]
    xo2 = [0.208996,]
    xn2 = [0.781,]
    xcfc11 = [2.783e-10,]
    xcfc12 = [5.027e-10,]
    return Dataset(
        data_vars={
            "play": variable(pressure, "Pa", "air_pressure"),
            "tlay": variable(temperature, "K", "air_temperature"),
            "xh2o": variable(xh2o, "mol mol-1", "mole_fraction_of_water_vapor_in_air"),
            "xco2": variable(xco2, "mol mol-1", "mole_fraction_of_carbon_dioxide_in_air"),
            "xo3": variable(xo3, "mol mol-1", "mole_fraction_of_ozone_in_air"),
            "xn2o": variable(xn2o, "mol mol-1", "mole_fraction_of_nitrous_oxide_in_air"),
            "xco": variable(xco, "mol mol-1", "mole_fraction_of_carbon_monoxide_in_air"),
            "xch4": variable(xch4, "mol mol-1", "mole_fraction_of_methane_in_air"),
            "xo2": variable(xo2, "mol mol-1", "mole_fraction_of_oxygen_in_air"),
            "xn2": variable(xn2, "mol mol-1", "mole_fraction_of_nitrogen_in_air"),
            "xcfc11": variable(xcfc11, "mol mol-1", "mole_fraction_of_cfc11_in_air"),
            "xcfc12": variable(xcfc12, "mol mol-1", "mole_fraction_of_cfc12_in_air"),
         },
         coords={
             "layer": (["z",], [1,])
         },
    )


if __name__ == "__main__":
    from numpy import arange
    from pyLBL import Database, Spectroscopy, HitranWebApi

    webapi = HitranWebApi("")
    database = Database("foo.db")
    database.create(webapi)
    dataset = create_circ_xarray_dataset()
    grid = arange(1., 5000., 1.)
    s = Spectroscopy(dataset, grid, database)
    print(s.list_molecules())
    for i in ["all", "gas", None]:
        output = s.compute_absorption(output_format=i)
        output.to_netcdf("out-" + str(i or "total") + ".nc")
