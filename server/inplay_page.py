import streamlit as st
from alert import create_alert,get_request_status,initialize_opsgenie

# Initialize Opsgenie with your API key
api_key = "db07dbc2-8353-4477-a21d-22c261aea506"
alert_api = initialize_opsgenie(api_key)



def show_page():
    if "outage_selection" not in st.session_state:
        st.session_state["outage_selection"] = None

    st.sidebar.header("Choose Affected Sport")
    inplay_options = ["Multiple/All", "Football", "Another single sport"]
    inplay_selection = st.sidebar.selectbox("", inplay_options)

    # Main body
    st.header("You selected:")
    if inplay_selection == "Multiple/All":
        st.write("Level of impact memo:")
        st.write(
            "- Critical - The function of all or a substantial part of a Service has failed, critically degrading the Customer’s operational performance. No practicable workaround."
        )
        st.write(
            "- Major - Customer experiences a material adverse impact on the service they can offer to their customers. The workaround is impractical or operationally difficult."
        )
        st.write(
            "- Moderate - The Reported Fault does not materially affect Customer’s Service."
        )
        st.write(
            "- Minor - The customer can work around the reported fault and the effect on Customer operation is minimal."
        )

        impact_categories = ["Critical Impact", "Major Impact", "Moderate/Minor Impact"]
        impact_selection = st.selectbox("", impact_categories)

        if impact_selection == "Critical Impact":
            if st.button("Show outage durations"):
                st.write("How long did the outage last since first detection?")
                outage_durations = [
                    "Under 15 minutes",
                    "15-30 minutes",
                    "Over 30 minutes",
                ]
                st.session_state["outage_selection"] = st.selectbox(
                    "", outage_durations
                )

            if st.session_state["outage_selection"] == "Under 15 minutes":
                with st.expander(
                    "Just normal escalation to developers for now.", expanded=False
                ):
                    st.write(" Keep monitoring SO duration if it is ongoing.")
                if st.checkbox("15-30 minutes"):
                    # Add your sample data here
                    st.write("Have Tier 1 Customers been affected?")
                    yes_clicked = st.checkbox("Yes")
                    no_clicked = st.checkbox("No")

                    if yes_clicked:
                        st.write("Escalate to Exec and Commercial level:")
                        yes_inputs = []
                        for i in range(14):
                            yes_inputs.append(
                                st.text_input(
                                    f"Enter information for {i+1}",
                                    key=f"yes{i+1}",
                                )
                            )
                        if st.button("Notify"):
                            st.write(f"You entered: {yes_inputs}")
                            create_alert(alert_api)

                    if no_clicked:
                        st.write("You clicked No.")
                        # Create 14 input forms for 'No'
                        no_inputs = []
                        for i in range(14):
                            no_inputs.append(
                                st.text_input(
                                    f"Enter information for 'No' {i+1}", key=f"no{i+1}"
                                )
                            )
                        if st.button("Notify"):
                            st.write(f"You entered: {no_inputs}")
                            create_alert(alert_api)

                if st.checkbox("Over 30 minutes"):
                    st.write("Your nested information for Over 30 minutes goes here.")
                    # Add your sample data here
                    st.write("Sample data for Over 30 minutes")

                if st.button("Back"):
                    st.session_state["outage_selection"] = None
                    st.experimental_rerun()
    elif inplay_selection is not None:
        st.write(f"InPlay: {inplay_selection}")