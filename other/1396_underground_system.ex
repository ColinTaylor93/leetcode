defmodule UndergroundSystem do
  @spec init_() :: any
  def init_() do
    case Agent.start_link(fn -> %{check_ins: %{}, routes: %{}} end, name: :underground_agent) do
      {:ok, _pid} -> :ok
      {:error, {:already_started, _pid}} ->
        Agent.update(:underground_agent, fn _ -> %{check_ins: %{}, routes: %{}} end)
    end
  end

  @spec check_in(id :: integer, station_name :: String.t, t :: integer) :: any
  def check_in(id, station_name, t) do
    Agent.update(:underground_agent, fn state ->
      put_in(state, [:check_ins, id], {station_name, t})
    end)
  end

  @spec check_out(id :: integer, station_name :: String.t, t :: integer) :: any
  def check_out(id, station_name, t) do
    Agent.update(:underground_agent, fn state ->
      {start_station, check_in_time} = Map.fetch!(state.check_ins, id)
      duration = t - check_in_time
      route = {start_station, station_name}
      {total_time, count} = Map.get(state.routes, route, {0, 0})

      state
      |> update_in([:check_ins], &Map.delete(&1, id))
      |> put_in([:routes, route], {total_time + duration, count + 1})
    end)
  end

  @spec get_average_time(start_station :: String.t, end_station :: String.t) :: float
  def get_average_time(start_station, end_station) do
    {total_time, count} = Agent.get(:underground_agent, fn state ->
      Map.fetch!(state.routes, {start_station, end_station})
    end)
    total_time / count
  end
end
