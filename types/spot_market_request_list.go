// Code generated by go-swagger; DO NOT EDIT.

package types

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"strconv"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/strfmt"
	"github.com/go-openapi/swag"
)

// SpotMarketRequestList spot market request list
//
// swagger:model SpotMarketRequestList
type SpotMarketRequestList struct {

	// spot market requests
	SpotMarketRequests []*SpotMarketRequest `json:"spot_market_requests"`
}

// Validate validates this spot market request list
func (m *SpotMarketRequestList) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateSpotMarketRequests(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *SpotMarketRequestList) validateSpotMarketRequests(formats strfmt.Registry) error {

	if swag.IsZero(m.SpotMarketRequests) { // not required
		return nil
	}

	for i := 0; i < len(m.SpotMarketRequests); i++ {
		if swag.IsZero(m.SpotMarketRequests[i]) { // not required
			continue
		}

		if m.SpotMarketRequests[i] != nil {
			if err := m.SpotMarketRequests[i].Validate(formats); err != nil {
				if ve, ok := err.(*errors.Validation); ok {
					return ve.ValidateName("spot_market_requests" + "." + strconv.Itoa(i))
				}
				return err
			}
		}

	}

	return nil
}

// MarshalBinary interface implementation
func (m *SpotMarketRequestList) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *SpotMarketRequestList) UnmarshalBinary(b []byte) error {
	var res SpotMarketRequestList
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
