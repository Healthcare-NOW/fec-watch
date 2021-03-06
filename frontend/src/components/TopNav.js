import {useSelector} from "react-redux";
import {breadcrumbsSelector} from "../selectors";
import {Route, Switch} from "react-router-dom";
import {dropRight, map, takeRight, isEmpty} from "lodash";
import {Breadcrumb, Container, Header} from "semantic-ui-react";
import React from "react";
import {routeMap} from "../App";
import healthcareNowLogo from "../HCNLogo.jpg";

export const TopNav = () => {
    const {isLoading} = useSelector(breadcrumbsSelector);
    return (
        <div>
            <Container align='center'>
            <div className='App-healthcare-now-logo'>
                <a href='https://healthcare-now.org'>
                    <img src={healthcareNowLogo} alt="Healthcare-NOW logo"/>
                </a>
            </div>
            <Header className='App-appName' as='h1'>Patients Over Profits Donation Tracker 2019-2020</Header>
            </Container>
            <div className='App-breadcrumbs'>
                {isLoading ? <span/> :
                    <Switch>
                        {map(routeMap, ({path, breadcrumbs}) => {
                            if (isEmpty(breadcrumbs)) return null;
                            const inactive = dropRight(breadcrumbs, 1);
                            const active = takeRight(breadcrumbs, 1);
                            return (
                                <Route exact path={path} key={path}>
                                    <Breadcrumb size="huge">
                                        {
                                            map(inactive, (BreadcrumbComponent) => (
                                                <>
                                                    <BreadcrumbComponent/>
                                                    <Breadcrumb.Divider icon="right chevron"/>
                                                </>
                                            ))
                                        }
                                        {
                                            map(active, (BreadcrumbComponent) => (
                                                <BreadcrumbComponent active/>
                                            ))
                                        }
                                    </Breadcrumb>
                                </Route>
                            );
                        })}
                    </Switch>
                }
            </div>
        </div>

    )
};